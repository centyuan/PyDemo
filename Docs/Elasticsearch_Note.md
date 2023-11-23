---
title: Elasticsearch Note
categories:
   - 中间件
tags: 
   - Elasticsearch
---



#### 基本概念

>**索引Index:**
>
>```
>一个索引就是相似特征的文档集合，同比预于mysql的表，mongodb的文档(**保存一个文档doc到elasticsearch中的过程也叫索引(indexing)**)
>```
>
>**映射mapping:**
>
>```
>处理数据的方式和规则(比如: 字段的数据类型，默认值，分析器，是否被索引，包括设置分片数(number_of_shards)和副本数(number_of_replicas))
>
>ES 的Mapping 类似于传统关系型数据库的表结构定义
>```
>
>**分片Shards:**
>
>```
>一个索引可以存储超出单个节点硬件限制的大量数据，所有索引分片数决定了一个索引的最大存储
>```
>
>**副本Replicas:**
>
>
>
>**什么是倒排索引?**
>
>```
>Elasticsearch分别为每个field都建立了一个倒排索引
>Term到所有包含该Term的文档的DocId列表的映射。ES 默认会对写入的数据都建立索引，并且常驻内存
>我们首先将每个文档的content域拆分成单独的词（我们称它为词条或tokens ），创建一个包含所有不重复词条的排序列表，然后列出每个词条出现在哪个文档
>总结:文档关键词到文档id的映射
>
>主要采用以下几种数据结构
>1.倒排索引:保存了每个term对应的docId的列表，采用skipList的结构保存，用于快速跳跃
>2.FST（Finite State Transducer）: 原理上可以理解为前缀树，用于保存term字典的二级索引，用于加速查询，可以在FST上实现单Term、Term范围、Term前缀和通配符查询等。内部结构如下
>3.BKD-Tree： KD-Tree是一种保存多维空间点的数据结构，主要用于数值类型(包括空间点)的快速查找。
>```
>
>
>
>**动态更新索引**
>
>引入了按段搜索的概念。**每一段本身都是一个倒排索引**



#### 路由计算

>当索引一个文档的时候,文档会被存储到一个主分片中,`需要路由计算来确定文档应该存到那个分片中`
>
>计算公式:
>
>shard = hash(rouging) % number_of_primary_shards   # 最后会得到一个数：0到number_of_primary_shards-1
>
>routing: 是一个可变值,默认为文档的**_id**
>
>number_of_primary_shards: 主分片数量
>
>所以索引创建时候确定了主分片数量后,就永远不能改变了，不然会导致之前所有路由的值都失效，文档在也找不到了



#### 文档操作流程

##### 文档写流程

>1.client向任一节点发送请求
>
>2.节点通过文档的_id确定文档属于那个分片，将请求转发到对应`主分片`的节点上
>
>3.主分片执行成功后，并发将请求转发到副本分片上去，所有副本都成功后，将向客户端返回成功信息
>
>**注意事项**
>
>```
>1.对于文档的新建，索引的创建和删除都写操作，必须在主分片上进行，然后在复制到副本上
>2.ES为了提高写入能力，采用并发写的方式，为了解决并发写过程中数据冲突问题，ES通过乐观锁控制(每个文档都有一个_version，文档修改时版本号递增)
>并发模式下，只要有副本在，写入延时最小也是两次单分片的写入耗时总和，效率会较低，但是这样的好处也很明显，避免写入后单个机器硬件故障导致数据丢失，在数据完整性和性能方面，一般都是优先选择数据，除非一些允许丢数据的特殊场景
>3.一旦所有的副本分片都报告写成功才会向协调节点报告成功，协调节点向客户端报告成功
>4.`ES为减少磁盘I/O次数，一般是每隔一段时间才会把数据写入磁盘持久化`
>对于内存数据丢失问题，ES借鉴数据库处理方式，增加Commitlog，在ES中叫translog(类似于mysql的binlog,用于宕机后内存数据的恢复，保存未持久化数据的操作日志)
>```
>
>

##### 文档读流程

>可以从主分片或任意副本分片检索文档
>
>1.向任一节点发送请求
>
>2.通过文档_id确定分片，由于 存在副本分片，通过轮训方式来确定访问那个节点的分片
>
>3.分片节点将文档返回给协调节点，协调节点在将文档返回给客户端
>
>在处理读取请求时，**协调结点在每次请求的时候都会通过轮询所有的副本分片来达到负载均衡**，已经被索引的文档可能已经存在于主分片上但是还没有复制到副本分片。在这种情况下，副本分片可能会报告文档不存在，但是主分片可能成功返回文档

##### 文档删除更新

>段是不可改变的，只是在 `.del` 文件中被 *标记* 删除
>
>**近实时搜索**
>
>按段搜索降低了文档从索引到可被搜素的延迟，但是还是不够(Commiting 提交到磁盘还是很慢)
>
>在Elasticsearch和磁盘之间是文件系统缓存：
>
>在内存索引缓冲区中的文档会被写入到一个新的段中。但是这里新段会被先写入到文件系统缓存—这一步代价会比较低，稍后再被刷新到磁盘—这一步代价比较高。不过只要文件已经在缓存中，就可以像其它文件一样被打开和读取了(**缓冲区的内容已经被写入一个可被搜索的段中，但还没有进行提交**)



#### 存储原理

>ES基于Lucene实现的，当添加一份文档时候，会经过一下流程
>
>1.Lucene进行分词等预处理
>
>2.将文档索引写入内存中，并将操作写入事务日志(translog，类似于mysql的binlog,保存未持久化数据的操作日志，用于宕机后内存数据恢复)
>
>3.Lucene每隔`refresh_interval`(配置项)时间将内存数据刷入到文件系统缓存中，称为segment，刷入文件系统缓存后，segment才可以被用于检索
>
>默认情况下，Lucene每隔30min或segment 空间大于512M，将缓存中的segment持久化落盘，称为一个commit point，此时删掉对应的transLog
>
>在Elasticsearch 中，写入和打开一个新段的轻量的过程叫做`refresh` 。**默认情况下每个分片会每秒自动刷新一次**。这就是为什么我们说Elasticsearch 是近实时搜索: **文档的变化并不是立即对搜索可见，但会在一秒之内变为可见**
>
>并不是所有情况都需要每秒刷新,可以设置refresh_interval，降低每个索引刷新频率，达到优化索引速度
>
>**段合并**
>
>```
>由于自动刷新每秒会创建一个新的段,这样会导致短时间内段的激增,段太多会消耗文件句柄并且每个请求都必须轮流检查每个段
>通过段合并来解决问题
>```
>
>

#### 文档查询的优化

>1.分片规模(为了让分片查询性能发挥到最优,需要对规模进行限制)
>
>2.增加副本数(分摊查询的负载)
>
>3.Mapping设计
>
>```
>1.ES 默认会建立索引，行存，列存。对于某些并不重要的字段，可以通过指定（index: false ， store: false ，doc_values: false）来关闭，以减少冗余存储成本
>2.ES 默认对于数值字段建立BKDTree 索引，但是倒排索引能够最大发挥Lucene 的查询性能。所以对于有限枚举值的数值字段，也建议使用keyword 类型以创建倒排索引
>```
>
>4.**查询 Routing 路由优化**
>
>```
>单个查询会扫描所有分片，容易遇到长尾效应，且大量节点在空转，可利用ES路由能力，大幅提高查询吞吐、降低长尾
>过写入时支持指定routing ，ES 会计算 target_shard_id = hash(routing) 将写入数据路由到指定分片上，这样在查询时，也可以通过指定routing，快速定位到目前数据所在的分片，查询的效率能够提升一个数量级
>```
>
>
>
>[ES查询优化攻略](https://zhuanlan.zhihu.com/p/647279604)

#### 文档写入速度的优化

>ES的默认配置是综合了数据的可靠性和写入程度,实际需要根据场景优化
>
>```
>1.加大Translog Flush，目的是降低Iops、Writeblock
>	Flush的目的将操作系统的文件缓存中的段持久化到硬盘，Translog 的数据量达到512MB 或者30 分钟时，会触发一次Flush
>2.增加Index Refresh 间隔，目的是减少Segment Merge 的次数
>  	新的数据写入索引时，Lucene 就会自动创建一个新的段，Lucene 将待写入的数据先写到内存中，超过1 秒（默认）时就会触发一次Refresh，然后Refresh 会把内存中的的数据刷新到操作系统的文件缓存系统中
>3.调整Bulk 线程池和队列
>4.优化节点间的任务分布
>5.优化Lucene 层的索引建立，目的是降低CPU 及IO
>6.大批量写的时候，可以先禁止Replica复制
>	设置index.number_of_replicas: 0 关闭副本。在写入完成后，Replica 修改回正常的状态
>```
>
>

#### ES节点和集群

##### 节点

>一个节点就是一个运行的ES实例,每个节点都有一个唯一的名称作为身份标识，如果没有设置名称，默认使用 UUID 作为名称
>每个节点都知道集群中任一文档的位置，可以直接将请求转发到任一节点，每个节点都可以扮演协调节点(coordinating node)角色



##### 节点角色

>ES中节点有角色的区分的，通过配置文件conf/elasticsearch.yml中配置以下配置进行角色的设定
>
>```
>node.master:  true/false
>node.data: true/false
>（1）仅为候选主节点
>（2）既是候选主节点也是数据节点
>（3）仅为数据节点
>（4）既不是候选主节点也不是数据节点
>```
>
>Mater节点：无需参与文档层面的变更和搜索，负责管理集群的变更(如索引的创建和删除，节点的加入和删除)
>
>data节点: 持有数据和倒排索引
>
>client节点: 将node.master和node.data都设置成false，那么该节点就是一个客户端节点，将请求路由到集群其他节点，扮演一个协调节点角色，用于负载均衡

##### 节点发现机制

>ZenDiscovery 是ES内置发现机制，提供`多播`和`单播`两种方式
>
>**多播:**
>
>```
>一个节点可以向多台机器发送请求(生产中不建议这样用,会产生大量不必要的通信)
>```
>
>**单播:(默认)**
>
>```
>当一个节点请求到单播列表中的成员时，就会得到整个集群所有节点的状态，然后请求master节点并加入集群
>```

##### 选主

>**选主流程**
>
>Es的master就是从activeMasters列表或者masterCandidates列表选举出来
>
>1.筛选activeMasters列表
>
>```
>Elasticsearch节点成员首先向集群中的所有成员发送Ping请求，elasticsearch默认等待discovery.zen.ping_timeout时间，然后elasticsearch针对获取的全部response进行过滤，筛选出其中activeMasters列表，activeMaster列表是其它节点认为的当前集群的Master节点
>在获取activeMasters列表的时候会排除本地节点，目的是为了避免脑裂问题
>```
>
>2.筛选masterCandidatess
>
>```
>masterCandidates列表是当前集群有资格成为Master的节点，在elasticsearch.yml中配置了如下参数，那么这个节点就没有资格成为Master节点，也就不会被筛选进入masterCandidates列表
>node.master:false
>```
>
>3.从activeMaters列表选举Master节点
>
>```
>activeMasters列表不为空，elasticsearch会优先从activeMasters列表中选举
>选举算法是Bully算法
>会涉及到优先级比较，选择优先级最高的，在选择id最小的节点
>```
>
>4.从masterCandidates列表选举Master节点
>
>```
>activeMasters列表节点为空，则从masterCandidates列表选举
>首先会判断masterCandidates列表成员数目是否达到了最小数目discovery.zen.minimum_master_nodes
>在比较节点拥有集群状态版本编号(让拥有最新集群状态节点成为master)，比较优先级和id
>```
>
>5.节点是master
>
>```
>上面流程会选举出一个**准master**节点
>准master节点等待其它节点的投票，有discovery.zen.minimum_master_nodes-1个节点投票认为当前节点是master，选举就成功，
>准master会等待discovery.zen.master_election.wait_for_joins_timeout时间，超时则就失败，失败会重新进行选举
>
>本地节点是Master时候:
>Master节点会开启错误检测(NodeFaultDetection机制)，它节点会定期扫描集群所有的成员，将失活的成员移除集群，同时将最新的集群状态发布到集群中，集群成员收到最新的集群状态后会进行相应的调整，比如重新选择主分片，进行数据复制等操作
>```
>
>6.节点不是master
>
>```
>当前节点判定在集群当前状态下如果自己不可能是master节点，首先会禁止其他节点加入自己，然后投票选举出准Master节点。同时监听master发布的集群状态(MasterFaultDetection机制)，如果集群状态显示的master节点和当前节点认为的master节点不是同一个节点，那么当前节点就重新发起选举。
>
>非Master节点也会监听Master节点进行错误检测，如果成员节点发现master连接不上，重新加入新的Master节点，如果发现当前集群中有很多节点都连不上master节点，那么会重新发起选举。
>```
>
>
>
>**脑裂问题**
>
>```
>集群中不同的节点对于master的选择出现了分歧，出现了多个master竞争,这种现象称为脑裂
>
>`脑裂问题可能的原因`
>1.网络问题: 节点访问不到Master，而选举新的Master，实际master并没有宕机
>2.节点负载: 主节点的角色既为master又为data，访问量较大时可能会导致ES停止响应造成大面积延迟，此时其他节点得不到主节点的响应认为主节点挂掉了，会重新选取主节点
>3.内存回收: data节点上的ES进程占用的内存较大，引发JVM的大规模内存回收，造成ES进程失去响应
>```
>
>**脑裂问题解决方式**
>
>```
>1.减少误判:discovery.zen.ping_timeout节点状态的响应时间，默认为3s，可以适当调大，如果master在该响应时间的范围内没有做出响应应答，判断该节点已经挂掉了。调大参数（如6s，discovery.zen.ping_timeout:6），可适当减少误判
>2.选举触发: discovery.zen.minimum_master_nodes:1
>当备选主节点的个数大于等于该参数的值，且备选主节点中有该参数个节点认为主节点挂了，进行选举。官方建议为（n/2）+1，n为主节点个数（即有资格成为主节点的节点个数）
>3.角色分离:即master节点与data节点分离，限制角色
>主节点配置为：
>	node.master: true node.data: false
>从节点配置为：
>	node.master: false node.data: true
>```
>
>





#### 三种ES基本操作

>1.使用request发送http请求
>
>2.使用官方提供的elasticsearch
>
>3.ORM包elasticsearch-dsl

##### 查询描述

```
1、must (must字段对应的是个列表，也就是说可以有多个并列的查询条件，一个文档满足各个子条件后才最终返回)
2、should (只要符合其中一个条件就返回)
3、must_not (与must相反，也就是说可以有多个并列的查询条件，一个文档各个子条件后才最终的结果都不满足)
4、filter(条件过滤查询，过滤条件的范围用range表示gt表示大于、lt表示小于、gte表示大于等于、lte表示小于等于)

bool查询总结
    must：与关系，相当于关系型数据库中的 and。
    should：或关系，相当于关系型数据库中的 or。
    must_not：非关系，相当于关系型数据库中的 not。
    filter：过滤条件。

range：条件筛选范围。
gt：大于，相当于关系型数据库中的 >。
gte：大于等于，相当于关系型数据库中的 >=。
lt：小于，相当于关系型数据库中的 <。
lte：小于等于，相当于关系型数据库中的 <=

1.1、term
1）term查询keyword字段。
term不会分词。而keyword字段也不分词。需要完全匹配才可。
2）term查询text字段
因为text字段会分词，而term不分词，所以term查询的条件必须是text字段分词后的某一个。
1.2.match
1）match查询keyword字段
match会被分词，而keyword不会被分词，match的需要跟keyword的完全匹配可以。
其他的不完全匹配的都是失败的。
2）match查询text字段
match分词，text也分词，只要match的分词结果和text的分词结果有相同的就匹配。
1.3.match_phrase
1）match_phrase匹配keyword字段。
这个同上必须跟keywork一致才可以。
2）match_phrase匹配text字段。
match_phrase是分词的，text也是分词的。match_phrase的分词结果必须在text字段分词中都包含，而且顺序必须相同，而且必须都是连续的。
1.4.query_string
1）query_string查询keyword类型的字段，试过了，无法查询。

2）query_string查询text类型的字段。

和match_phrase区别的是，不需要连续，顺序还可以调换。

```



##### Elasticsearch包操作

```
from elasticsearch import Elasticsearch
es = Elasticsearch([{"host": "123.60.180.204", "port": 9200}], timeout=3600)
# 1.查询
query = {
    "query": {
        "match_all": {}
    }
}
re = es.search(index="teacher", body=query)

# term/terms查询,terms可以指定多个条件
query = {
    "query": {
        "term": {
            # "name":["汪老师","老师"]
            "name": "老师"
        }
    }
}
result = es.search(index="teacher", body=query)
print(result)

# 范围查询
 query = {
  "query":{""}
  }

# 2.插入单条数据
result = es.index(index="teacher", doc_type="_doc", body={
"name": "老师名称",
"description": "是个可爱的语文老师",
"age": "20",
"sex": "男"
})
# 3.插入多条数据
doc = [
{"index": {"_index": "teacher", "_type": "_doc", "_id": 1}},
{"name":"汪老师","description":"语文老师","age":26,"sex":"女"},
{"index": {"_index": "teacher", "_type": "_doc", "_id": 2}},
{"name": "何老师", "description": "政治老师", "age": 26},
{"index": {"_index": "teacher", "_type": "_doc", "_id": 2}},
{"name": "老师", "description": "老师", "sex": "女"}
]
es.bulk(index="teacher",doc_type="_doc",body=doc)
```



##### elasticsearch-dsl

```
from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested, Boolean, analyzer, InnerDoc, Completion, Keyword, Text, Integer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["123.060.180.204:9200"])
es = connections.create_connection(hosts=["127.0.0.1:9200"], timeout=20)
res = Search(using=es).index("test_index").query()

class Article(Document):
    title = Text(fields={'title': Keyword()})
    author = Text()

    class Index:
        name = 'myindex'  # 索引名

if __name__ == '__main__':
    Article.init()  # 创建映射
    # 保存数据
    article = Article()
    article.title = "test"
    article.author = "lxx"
    article.save()  # 保存数据
# # 查询数据
# s = Article.search()
# s = s.filter('match', title="test")
# results = s.execute()
# print(results)

# # 删除数据
# s = Article.search()
# s = s.filter('match', title="test").delete()
# # 修改数据
# s = Article().search()
# s = s.filter('match', title="test")
# results = s.execute()
# print(results[0])
# results[0].title = "xxx"
# results[0].save()
```



>

#### Others

    # ./bin/elasticsearch-plugin install https://github.com/NLPchina/elasticsearch-analysis-ansj/releases/download/v7.6.2/elasticsearch-analysis-ansj-7.6.2.0-release.zip
    
     # docker run --name my_es7 -p 9200:9200  -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms84m -Xmx512m" -v /root/my_elasticsearch/data:/usr/share/elasticsearch/data -v  /root/my_elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.6.2

 # 