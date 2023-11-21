#### 一:三种ES基本操作

>1.使用request发送http请求
>
>2.使用官方提供的elasticsearch
>
>3.ORM包elasticsearch-dsl

####  二:查询描述

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



####  三:Elasticsearch包操作

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



#### 四:elasticsearch-dsl

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



#### 五:性能优化

>**写优化：**
>
>尽量采用批量提交，合理设置磁盘，设置段合并速度，减少refresh次数（从内存刷新到文件缓存中），
>
>加大flush设置（多大的值之后从文件缓存中flush到磁盘上），减少副本的数量，
>
>内存，文件缓存系统，磁盘
>
>**读优化：**
>
>避免大结果集合深翻
>
>选择合适的路由
>
>合理的设置SearchType
>
>定期删除.del文件
>
>合理的设置堆大小

#### Others

    # ./bin/elasticsearch-plugin install https://github.com/NLPchina/elasticsearch-analysis-ansj/releases/download/v7.6.2/elasticsearch-analysis-ansj-7.6.2.0-release.zip
    
     # docker run --name my_es7 -p 9200:9200  -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms84m -Xmx512m" -v /root/my_elasticsearch/data:/usr/share/elasticsearch/data -v  /root/my_elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.6.2
 # 
