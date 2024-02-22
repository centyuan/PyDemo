---
title: Redis Note
categories:
   - Redis
tags:
   - Redis

---

#### 概述

> REmote DIctionary Server(Redis) 是一个由 Salvatore Sanfilippo 写的 key-value 存储系统，是跨平台的非关系型数据库。
>
>  是一个开源的使用 ANSI C 语言编写、遵守 BSD 协议、支持网络、可基于内存、分布式、可选持久性的键值对(Key-Value)存储数据库，并提供多种语言的 API。
>
> **单线程:** Redis是单线程的(所谓多线程,是说Redis处理客户端的请求及执行命令，并不是整个Redis都是单线程)
>
> 4.0后有了多线程,处理命令请求的核心模块,其他地方已经有了多线程比如:后台删除对象，生成dump文件，以及6.0中网络I/O实现了多线程
>
> **IO多路复用机制:**
>
> 多路指的是多个TCP连接,复用指的是一个或多个线程，`I/O` 多路复用的核心原理就是不再由应用程序自己来监听连接，而是由服务器内核替应用程序监听
>
> 在redis中，多路复用有多重实现如: select,epoll,evport,kqueue
>
> 通俗解释:
>
> ```
> 以买奶茶为例:你点了一杯奶茶
> 同步阻塞IO:，啥也不干，就等着,没做其他的叫阻塞，等奶茶叫同步
> 同步非阻塞IO:一会刷刷抖音，一会瞅瞅奶茶好没，没阻塞干其他的，但是在同步等奶茶好没
> 异步阻塞IO:服务员给你个小票,好了通知你来取,但是你没干其他的，叫阻塞，好了通知你叫异步,这个最傻
> 异步非阻塞IO:服务员给你个小票,好了通知你来取，你可以刷刷抖音
> 事件驱动机制:
>  奶茶做好了并不知道是谁的，就需要每个问下，这个就是select模型,最多只能监听1024个socket,poll解决了这个限制
>  奶茶做好了也不知道是谁的,就大声喊下“某某的奶茶好了",这就是多路复用中的epoll模型
>  ```
>  



#### 1.基础命令

```plaintext
select number(0-15):切换数据库
dbsize:查看当前数据库的key的数量
flushdb:清空当前数据库
flushall:清空所有库
keys *:查看当前库所有key
exists key:key是否存在
type key:查看key类型
del key:删除
unlink key:非阻塞删除,先将keys从keyspaces删除,真正的删除在后续异步操作中
expire key 10:设置10秒过期时间
ttl  key :-1表示永不过期,-2表示已过期
info memory:查看内存使用情况
config set maxmemory 100mb:动态命令配置redis最大内存 config get maxmemory
淘汰策略:
1.noeviction(默认,只读不写)
2.lru:最近最少使用(allkeys-lru,volatile-lru)
3.random:随机淘汰(allkeys-random,volatile-random)
4.ttl:过期时间淘汰(volatile-ttl:配置过期的键中删除马上过期的,volatile-lfu:配置过期键中删除使用频率最少的)
5.allkeys-lfu:所有键删除使用频率最少的
定时(每个过期key都需创建一个定时器)/惰性(访问key,判定key是否过期)/定期
```



![Redis数据类型](https://pic4.zhimg.com/v2-83d9146cac1b288a30fbb841534b6e73_r.jpg)

#### 2.五大基本数据类型

> 在Redis有个核心对象**redisObject**,用来表示String,Hash,List,Set,ZSet 

> ##### 1.String字符串
>
> >字符串是一种基本的数据类型，Redis对字符串进行了特别设计，一种二进制安全的字符串对象，可以包含任何数据。比如jpg图片或者序列化的对象。string 类型的值最大能存储 512MB,类似Java的ArrayList,pyton的list,在第一次append也会超额分配,来减少频繁的内存分配
>
> 底层实现:动态字符串
>
> ```plaintext
> 底层数据结构存储方式有三种:
> int, raw,embstr
> 1.如果是整数值就会使用int的存储方式
> 2.使用【简单动态字符串SDS】(Simple dynamic string):
> 如果是字符串且长度大于32个字节,,encoding设置为raw
> 如果是字符串且长度小于等于32个字节,encoding设置为embstr
> ```
>
> **SDS与c语言字符串对比**
>
> ```
> redis在SDS上对c语言的字符串做了自己的设计和优化，具体优势有以下几点：
> （1）c中字符串并不会记录长度，每次获取字符串的长度都会遍历得到，[时间的复杂度是O(n)]，而Redis中获取字符串只要读取len的值就可，[时间复杂度变为O(1)]。
> （2）c中两个字符串拼接，没有分配足够长度的内存空间就「会出现缓冲区溢出的情况」；SDS会先根据len属性判断空间是否满足要求，若是空间不够，会进行空间扩展，所以不会出现缓冲区溢出的情况。
> （3）SDS还提供「空间预分配」和「惰性空间释放」两种策略。在字符串分配空间时，分配的空间比实际要多，这样就能减少连续的执行字符串增长带来内存重新分配的次数。
> 当字符串被缩短的时候，SDS也不会立即回收不适用的空间，而是通过free属性将不使用的空间记录下来，等后面使用的时候再释放。
> 
> 具体的空间预分配原则是：「当修改字符串后的长度len小于1MB，就会预分配和len一样长度的空间，即len=free；若是len大于1MB，free分配的空间大小就为1MB」。
> 
> （4）SDS是二进制安全的，除了可以储存字符串，还可以储存二进制文件（如图片、音频，视频等文件的二进制数据）；
> 而c中字符串是以空字符(\0)串作为结束符，一些图片中含有结束符，因此不是二进制安全的。
> 
> ```
>
> 应用场景: 存储图片，统计粉丝数
>
> 
>
> ##### 2.List列表
>
> >quicklist: 将多个ziplist使用双向指针串起来,即满足快速插入删除,又不会出现太大的空间冗余
>
> 底层实现：
>
> Redis3.2之前:
>
>   - 列表中元素较少和长度较小时: ziplist(压缩链表)
>
>    - 列表中元素角度和长度较大时: linkedlist(双向链表)
>
> **在 Redis 7.0 中，压缩列表数据结构已经废弃了，交由 listpack 数据结构来实现了。**
>
>   Redis3.2之后：quicklist
>
> ###### ziplist
>
> ```
> 是一组连续内存块组成的顺序的数据结构,能够节省空间,使用多个节点来存储数据
> **压缩列表并不是以某种压缩算法进行压缩存储数据，而是它表示一组连续的内存空间的使用，节省空间**
> 内存结构图如下:
> | zlbytes | zltail | zllen | entry1 | entry2 ... | zlend |
> zlbytes: 4个字节大小,记录压缩列表占用内存的字节数
> zltail: 4个字节大小,记录尾节点距起始位置的偏移量,用于快速定位到尾节点
> zllen: 2个字节大小,记录列表表中的节点数
> entry: 列表中一个节点
>    entry由三部分组成:
>    1.previous_entry_ength: 表示前一个节点entry的长度,因为地址是连续的，可用于计算前一个节点的地址
>    2.encoding: 保存的是content的内容类型和长度
>    3.content: 保存每个节点内容
> zlend: 表示压缩列表的特殊结束符号 '0xFF'
> 总结:
> ziplist的优点是内存紧凑，访问效率高，缺点是更新效率低，并且数据量较大时，可能导致大量的内存复制
> ```
>
> ###### linkedlist
>
> ```
> 和普通链表一样,指向前后节点的指针
> 插入/修改/更新的时间复杂度:O(1)
> 查询时间复杂度: O(n)
> 
> 链表的特性：
> 每一个节点都有指向前一个节点和后一个节点的指针。
> 头节点和尾节点的prev和next指针指向为null，所以链表是无环的。
> 链表有自己长度的信息，获取长度的时间复杂度为O(1)。
> 总结：
> linkedlist的优点是节点修改的效率高，但是需要额外的内存开销，并且节点较多时，会产生大量的内存碎片
> ```
>
> ###### quicklist
>
> ```
> 就是双向链表与压缩列表的组合,包含多个内存不连续的节点，但每个节点本身就是一个 ziplist
> ```
>
> 应用场景:阻塞队列
>
> 
>
> ##### 3.Hash哈希
>
> >当field-value长度较短个数较少: ziplist,否则使用: hashtable
> >
> >当hash对象可以同时满足一下两个条件时，哈希对象使用ziplist编码：
> >
> >   1.哈希对象保存的所有键值对的键和值的字符串长度都小于64字节
> >
> >​    2.哈希对象保存的键值对数量小于512个
>
> 底层实现方式为：hashtable,ziplist,其中hashtable的key是String类型
>
> ###### ziplist压缩列表
>
> ```
> 同上
> 使用ziplist的优点:
>   1.相比hashtable,ziplist结构减少了指针,节约了内存
>   2.相比linkedlist,ziplist存储时内存分配是连续的,查询更快
> ziplist如何实现hash存储的:
>   将同一个键值对的两个节点紧挨着保存,保存键的节点在前,保存值的节点在后,新加入的键值对,放在压缩列表表尾
> ```
>
> ###### hashtable
>
> ```
> 和字典底层类型类似，通过链地址法解决hash冲突
> 当对其扩容时，需要rehash,但是Redis不是一次性把所有数据全部rehash成功，这样会导致Redis对外停止服务,Redis内部为了解决这种情况采用【渐进式rehash】,将所有rehash的操作分成多步进行，直到都rehash完成
> ```
>
> 应用场景:存储用户数据,分布式生成唯一id
>
> 
>
> ##### 4.Set集合
>
> >一个无序的、自动去重的集合数据类型
>
> 底层实现: hashtable,intset 
>
> ###### hashtable
>
> ```
> 同上
> 其实是value为null(所有value指向同一个内部值)的hash表
> ```
>
> ###### intset
>
> ```
> intset叫整数集合，查询方式一般采用二分查找法，实际查询复杂度也就在log(n)
> 使用条件:
>  - 元素个数不少于默认值512
>  - 元素可以用整数表示
> intset底层结构:
>   uint32_t encoding; //编码类型
>   uint32_t length;   //元素的数量
>   int8_t contents [] //元素的数组
> ```
>
> 应用场景:去重、抽奖、共同好友、二度好友
>
> 
>
> ##### 5.Zset有序集合
>
> >有序（score从小到大排序，score相同则元素字典序），自动去重的集合数据类型
>
> 底层实现: ziplist 和skiplist(跳跃表)
>
> ###### ziplist
>
> ```
> 同上
> 满足以下两个条件使用ziplist，其他时候使用skiplist:
>  1. 有序集合元素数量小于128个
>  2. 所有元素长度小于64字节
> ```
>
> ###### skiplist
>
> ```
> 跳跃表是一种有序的数据结构,每个节点维持多个指向其他节点的指针，从而能快速访问
> skiplist由如下几个特点：
>  1.有很多层组成，由上到下节点数逐渐密集，最上层的节点最稀疏，跨度也最大。
>  2.每一层都是一个有序链表，只扫包含两个节点，头节点和尾节点。
>  3.每一层的每一个节点都含有指向同一层下一个节点和下一层同一个位置节点的指针。
>  4.如果一个节点在某一层出现，那么该以下的所有链表同一个位置都会出现该节点。
> ```
>
> 应用场景:在实现排序类型的业务是比较常见的
>
> 如:最热门帖子,排行榜
>
> 参考:[Redis五种数据类型](https://zhuanlan.zhihu.com/p/148562122)

```
Redis 中支持的数据类型到 6.0.6 版本，一共有 9 种。分别是：
Binary-safe strings（二进制安全字符串）
Lists（列表）
Sets（集合）
Sorted sets（有序集合）
Hashes（哈希）
BitMap（2.2 版新增）：二值状态统计的场景，比如签到、判断用户登陆状态、连续签到用户总数等；
HyperLogLog（2.8 版新增）：海量数据基数统计的场景，比如百万级网页 UV 计数等；
GEO（3.2 版新增）：存储地理位置信息的场景，比如滴滴叫车；
Stream（5.0 版新增）：消息队列，相比于基于 List 类型实现的消息队列，有这两个特有的特性：自动生成全局唯一消息ID，支持以消费组形式消费数据
```



#### 3. 操作命令

##### 1.String

```
# nx不存在时才会成功,ex设置过期时间
set cent bingxi nx ex 20
set cent bingxi
# 取值的范围
getrange cent 0 3
# 设置和过期时间
setex cent 20 bingxi
# 设置新值并返回旧值
getset cent newbingxi
# 设置多个key value
mset k1 v1 k2 v2 k3 v3
# setnx key:不存在成功
setnx cent bingxi
# msetnx 设置多个:都不存在才成功
msetnx k11 v11 k22 v22
get cent
# 取多个key
mget k1 k2 k3
# 取值的范围
getrange cent 0 3
# 值里面追加
append cent yuan
# 获取key长度
strlen cent
# 数字类型值加1  incr操作是原子性的:不会被线程调度机制打断
incr cent
# 数字类型加步长
incrby cent 10
# 数字类型值减1
decr cent
# 数字类型减步长
decrby cent 10
# 发布订阅
subscribe channel_yuan  # 订阅频道
publish channel_yuan helloworld # 推送消息到频道
```



##### 2.List

```
# 从左边插入一个或多个 ###从左边结果为n a u y
lpush cent y u a n
# 从右边插入一个或多个 ###从右边结果为y u a n
rpush cent y u a n
# 从左边/右边吐出一个值
lpop/rpop key
# 从key1列表右边吐出一个值,插到key2列表左边
rpoplpush key1 key2
lrange cent 1 4:取值  ### 0 -1:取所有
# 按照索引下表获得元素
lindex cent 2
# 获取列表长度
llen cent
# 在列表value值后面或前面插入一个新值
linsert cent after/before <value> <new_value>
# 将列表2的位置的值替换成newvalue
lset cent 2 newvalue
# 删除（指定值进行删除）
lrem <key> <n> <value>
```

##### 3.Hash

```
# 添加数据
hset <key> <field> <value>
# 取出数据
hget <key> <field>
# 批量设置多个值
hmset <key> <field1> <value2> <field2> <value2>
# 查看hash中field是否存在
hexists <key> <field>
# 查看hash中所有field
hkeys <key>
# 查看hash中所有value
hvals <key>
# hash对应field加上n
hincrby <key> <field> n
# 添加hash中对应field:当field不存在时
hsetnx <key> <field> <value>
```

##### 4.Set

```
# 添加，第二次插入相同元素将被忽略
sadd <key> <value1> <value2>
# 取集合所有值
smembers <key>
# 判断值是否在集合中,有返回,无返回0
sismember <key> <value>
# 返回集合元素个数
scard <key>
# 删除集合中某些值
srem <key> <value1> <value2>
# 随机吐出一个值
spop <key>
# 随机从集合取出n个值
srandmember <key> n
# 把集合中某个值移动到另一个集合
smove <source> <destination> value
# 返回两个集合的交集
sinter <key1> <key2>
# 返回两个集合并集
sunion <key1> <key2>
# 返回两个集合的差集,key1中的,不包含key2的
sdiff <key1> <key2>
```

##### 5. ZSet

```

# 添加元素
zadd <key> <score1> <value1> <score2> <value2>
# 取出所有值
zrange <key> 0 -1
# 取出值和评分
zrange <key> 0 -1 withscores
# 取出评分在min,max之间的值
zrangebyscore <key> min max          # zrevrangebyscore 从大到小
# 增加value对应的score n
zincrby <key> n <value>
# 删除
zrem <key> <value>
# 统计score在min,max之间元素个数
zcount <key> min max
# 返回value对应的排名 从0开始
zrank <key> <value>

# 6.redis6的新数据类型
Bitmaps实现了对位的操作字符串
# 设置值 key 偏移量
setbit <key> offset 1
# 取值
getbit <key> offset
```

详细参考:[redis使用介绍](https://www.runoob.com/w3cnote/python-redis-intro.html)



#### 4.Redis事务

>Redis事务(transaction)可以理解为一个打包的批量执行脚本，多个命令缓存在服务端,没有像Mysql关系型数据库事务隔离级别的概念，**不能保证原子性操作,中间某条指令的失败不会导致前面已做指令的回滚,也不会造成后续的指令不做**
>
>**特点**:
>
>```
>1.命令执行异常情况:命令执行时候出现异常,不影响其他命令的执行。
>2.指令或参数错误:命令入队失败,整个事务被取消。
>```
>
>**事务使用:**
>
>```
>1.multi开启事务:redis会将后续命令逐个放入队列中，
>
>	multi
>
>2.多个命令(入队时:命令失败,其他命令都不会执行,执行时:会跳过错误命令继续执行)
>
>	SET book_name "c++ plus"
>	SADD tag "C++" "Programming" "Mastering Series"
>
>3. EXEC执行事务(执行时:命令失败,不影响其他命令)
>
>	EXEC
>
>4.discard取消事务(放弃事务中所有命令)
>
>5.WATCH、UNWATCH在事务中用于乐观锁
>
>	在multi之前,watch监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断，EXEC会放弃队列中所有命令
>```
>
>**为什么Redis不支持事务回滚:**
>
>```
>多数事务失败是语法错误或数据结构类型错误导致的，语法错误在命令入队检查，类型错误在执行时检查,Redis为提升性能而采用这种简单事务
>```



#### 5.管道Pipeline

>管道技术(Pipeline)是客户端提供的一种批处理技术，用于一次处理多个 Redis 命令，从而提高整个交互的性能
>
>事务：是服务端行为，事务会被缓存，一起执行

>redis是基于客户端-服务端模型以及请求/响应协议的TCP服务,服务器进程会系统调用read()读取消息,处理完成后调用write把返回结果写入,这一过程涉及用户态到内核太的切换，管道使read/write一次处理多个命令,可以解决多个命令执行时的网络等待
>
>通常一个请求会遵循以下步骤:
>
>​	1.客户端向服务端发送一个请求,并监听Socket返回,通常是阻塞模式,等待服务响应
>
>​	2.服务端处理命令,并将结果返回客户端
>
>总结:如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令,不具有原子性,且并不是管道中命令越多越好(这个会消耗一定内存)



#### 6.配置说明

```
**redis.conf**
# 开启远程访问
	注释bind 127.0.0.1
	关闭保护模式:protected-mode no
tcp-backlog 511     # tcp-backlog未完成三次握手队列+已完成三次握手队列(高并发提升客户端连接,改成更大的值)
timeout 0           # 连接超时配置 0为永不超时,秒为单位
tcp-keepalive 300   # 300秒执行一次心跳检测,来决定是否释放连接
requirepass 123456  # 设置密码
conig set requirepass 123456   # 命令设置
maxclients 10000    # 设置客户端最大连接数
daemonize yes  # 设置后台启动
slave-priority 100   # 哨兵模式配置优先级 值越小优先级越高
maxmemory 3G         # 置内存大小一般为3G
dbfilename dump.rdb  # 配置RDB持久化文件名
rdbcompression yes   # 指定存储至本地数据库时是否压缩数据

#多实例关闭,指定端口关闭:redis-cli -p 6379 shutdown
```

#### 7.Redis持久化方案

>Redis是基于内存的key-value数据库,数据保存在内存中,为此提供了数据持久化,防止内存数据丢失，redis启动后会加载持久化文件
>
>分为RDB和AOF两种方式

##### RDB(Redis DataBase:默认持久化方式)

>RDB是默认持久化方式,基于快照一次的全量备份,即周期性的把redis当前内存中的全量数据写入到一个快照文件中(周期时间可以通过配置来修改,默认文件名dump.rdb)
>
>**命令方式**
>
>save(生产中一般不使用)：Reids save命令执行一个同步保存操作，将当前Redis实例的所有数据快照(snapshort)以RDB文件的方式保存到磁盘
>
>bgsave：bgsave执行后，会立刻返回OK，Redis 会fork一个子进程，原来的redis主进程继续执行后续操作，新fork的子进程负责将数据保存到磁盘，然后退出
>
>区别：
>
>- save是**同步**持久化数据，而bgsave是**异步**持久化数据。
>- `save`不会fork子进程，通过**主进程**持久化数据，会**阻塞**处理客户端的请求，而`bdsave`会`fork`子进程持久化数据，同时还可以处理客户端请求，高效。
>- save**不会消耗内存**，而bgsave**会消耗内存**。
>
>**相关配置**
>
>```
># 生成的文件名称
>dbfilename dump.rdb
># 路径
>dri /var/lib/redis
># yes表示Redis无法写入硬盘了,关闭Redis的写操作
>stop-writes-on-bgsave-error yes
># yes表示持久化文件压缩 
>rdbcompression yes
># yes表示持久化之前检测完整性,会增加大约10%性能消耗
>rdbchecksum yes
>```
>
>**持久化触发时机:**
>
> 1.save:使用save命令手动触发
>
> 2.bgsave: 使用bgsave命令手动触发
>
> 3.自动化:配置文件中配置 save
> ```
> save 900 1    # 表示900秒内如果至少有1个key值变化，则进行持久化保存数据
> save 300 10   # 表示300秒内如果至少有10个key值发生变化，则进行持久化
> save 60 10000 # 表示60秒内如果至少有10000个key值发生变化，则进行持久化
> ```
>
>**优缺点**
>
>```
>RDB持久化的文件是紧凑的二进制文件
>优点:
>1.适合于大规模的数据恢复，并且还原速度快(redis服务启动后会找到dump.rdb自动恢复)
>2.生成多个数据文件，适合冷备份
>3.fork子进程处理，对外提供的读写影响小
>缺点:
>1.占用两倍内存
>2.会丢失最后一次快照数据
>```
>
>

##### AOF(Append Only File)

>AOF持久化机制是以日志的形式记录Redis中的每一次的增删改操作，不会记录查询操作，以文本的形式记录，打开记录的日志文件就可以查看操作记录
>
>默认是不开启的
>
>**相关配置**
>
>```
>appendonly yes  # 开启AOF
>appendfilename "appendonly.aof"   # 配置生成的文件名
># 备份模式
>appendfsync always/everysec/no
>```
>
>**持久化触发时机**
>
>AOF带来的持久化更加安全可靠，默认提供**三种**触发机制
>
>```
>AOF带来的持久化更加安全可靠，默认提供三种触发机制
>no：服务器不主动调用 fsync 函数，由操作系统决定何时将缓冲区里面的命令写入到硬盘。这种模式下，服务器遭遇意外停机时，丢失命令的数量是不确定的，所以这种策略，不确定性较大，不安全。
>always：服务器每写入一个命令，就调用一次 fsync 函数，将缓冲区里面的命令写入到硬盘。这种模式下，服务器出现故障，也不会丢失任何已经成功执行的命令数据，但是其执行速度较慢。
>everysec(默认)：服务器每一秒调用一次 fsync 函数，将缓冲区里面的命令写入到硬盘。这种模式下，服务器出现故障，最多只丢失一秒钟内的执行的命令数据，通常都使用它作为 AOF 配置策略
>```
>
>**优缺点**
>
>```
>优点:
> 1.AOF更好保证数据不会被丢失，最多只丢失一秒内的数据
> 2.通过fork一个子进程处理持久化操作，保证了主进程不会进程io操作，能高效的处理客户端的请求
> 3.AOF的日志文件的记录可读性非常的高
>缺点:
> 1.相同数据，AOF文件大于RDB(日志文件很多重复的操作，甚至是无效的操作，导致日志文件越来越大)
> 2.AOF恢复速度比RDB慢
>```
>
>**AOF重写机制**
>
>```
>日志文件很多无效操作,通过bgrewriteaof命令。将内存中的数据以命令的方式保存到临时文件中，同时会fork出一条新进程来将文件重写。
>重写操作也会fork一个子进程来处理重写操作，重写以内存中的数据作为重写的源，避免了操作的冗余性，保证了数据的最新
>```

##### 混合持久化

>在redis4.0后混合持久化（RDB+AOF）对重写的优化，4.0版本的混合持久化默认是关闭的，可以通过以下的配置开启混合持久化
>
>```
>aof-user-rdb-preamble no
>```
>
>混合持久化结合**RDB持久化**和**AOF持久化**的优点，由于绝大部分的格式是RDB格式，加载速度快，增量数据以AOF方式保存，数据更少的丢失

总结:
>rdb适合大规模的数据恢复，由于rdb时异快照的形式持久化数据，恢复的数据快，在一定的时间备份一次，而aof的保证数据更加完整，损失的数据只在秒内。
>
>具体哪种更适合生产，在官方的建议中两种持久化机制同时开启



#### 8.淘汰策略

>Redis提供了**6种的淘汰策略**，其中默认的是`no-eviction`，这6中淘汰策略如下：
>
>1. `no-eviction`(**默认策略**)：不删除策略,若是内存的大小达到阀值的时候，所有申请内存的指令都会报错。
>2. `allkeys-lru`：在所有key中优先删除最近最少使用(less recently used ,LRU) 的 key。
>3. `volatile-lru`：所有**设置了过期时间的key使用LRU算法**进行淘汰。
>4. `allkeys-random`：所有的key使用**随机淘汰**的方式进行淘汰。
>5. `volatile-random`：所有**设置了过期时间的key使用随机淘汰**的方式进行淘汰。
>6. `volatile-ttl`：在设置了过期时间（expire ）的key中优先删除剩余时间(time to live,TTL) 短的key。。



#### 9.过期键删除策略

>**1、** 定时删除:创建一个定时器，定时的执行对key的删除操作。
>
>**2、** 惰性删除:每次只有再访问key的时候，才会检查key的过期时间，若是已经过期了就执行删除。
>
>**3、** 定期删除:每隔一段时间，就会检查删除掉过期的key。至于要删除多少过期键，以及要检查多少个数据库，则由算法决定。



#### 10.Redis集群方式

>1.主从复制
>
>2.哨兵sentinel
>
>3.Cluster

##### 1.主从

>一主二从,薪火相传,反客为主
>	master： read/wirte
>	slave:    only read 
>一般是读写分离,master负责write，slave负责read，slave要变成master需要手动slaveof加入,master挂了重启不影响主从之间关系
>
>**配置流程:**
>
>```
>#1.创建/myredis文件夹
>#2.创建redis6379.conf,redis6380.conf,redis6381.conf
>#3.修改各自配置文件
>include /myredis/redis.conf
>pidfile /var/run/redis_6379.pid
>port 6379
>dbfilename dump6379.rdb
>#4.启动几个redis redis-server /myredis/redis6379.conf
>#5.查看主从情况:info replication
>#6.设置主从:slaveof 127.0.0.1 6379
>
>```
>
>**主从同步流程:**
>
>```
>1.slave启动后向master发送SYNC命令,master收到请求后,使用bgsave保存快照(RDB持久化),期间执行的些命令会被缓存起来
>2.master将快照发给slave,并且继续缓存期间的写命令
>3.slave收到快照后就会加载到内存中
>4.最后master将缓存的命令同步给slave       
>```



##### 2.哨兵模式

>基于主从模式,增加了哨兵来监控与自动处理故障
>
>哨兵模式有以下的优点（功能点）：
>
>1. **监控**：监控master和slave是否正常运行，以及哨兵之间也会相互监控
>2. **自动故障恢复**：当master出现故障的时候，会自动选举一个slave作为master顶上去,选举算法**Raft算法**
>
>**配置流程:**
>
>```
># 1.创建sentinel.conf
>sentinel monitor mymaster 127.0.0.1 6379 1
>mymaster:为监控对象起的名称,1为至少有多少哨兵同意
># 2.启动哨兵
>redis-sentinel /myredis/sentinel.conf
># 选举new master策略
>1.选择优先级靠前的
>2.选择偏移量最大的(偏移量指获得原主机数据最全的)
>3.选择runid最小的slave从服务(Redis实例启动后随机生成一个40位的runid)
>```
>
>当哨兵启动后，会与master建立一条连接，用于订阅master的`_sentinel_:hello`频道,该频道用于获取监控该master的其它哨兵的信息。并且还会建立一条定时向master发送INFO命令获取master信息的连接
>
>**当哨兵与master建立连接后，定期会向（10秒一次）master和slave发送INFO命令，若是master被标记为主观下线，频率就会变为1秒一次**
>
>

##### 3.Cluster集群配置

>集群模式实现了数据的分布式存储和数据的分片,每个节点存储不同内容
>
>**Redis Cluster:**
>
>```
>**多主多从，去中心化**：从节点作为备用，复制主节点，不做读写操作
>**不支持处理多个key**：因为数据分散在多个节点，在数据量大高并发的情况下会影响性能
>**支持动态扩容节点**：算是Rerdis Cluster最大的优点之一
>**节点之间相互通信，相互选举，不再依赖sentinel**：准确来说是主节点之间相互“监督”，保证及时故障转移
>```

>```
># 集群实现扩容,集群不支持多键操作
>1. 每个redis.conf加上集群配置
>cluster-enabled yes                   # 打开集群
>cluster-config-file nodes-6379.conf   # 设置节点配置文件名
>cluster-node-timeout 15000            # 设置节点失联时间单位为毫秒,超过该时间,集群自动进行主从切换
>
>2.启动每个Redis实例 redis-server /myredis/redis.conf,确保nodes-xxxx.conf等文件都生成
>
>3.在redis src下执行依赖ruby环境,实现redis实例合成集群
># 1.表示一主一从
>	redis-cli --cluster create --cluster-replicas  1 ip:port ip2:port2
># 集群连接-c
>	redis-cli -c -p 6379
># 查看集群状态
>	cluster nodes
># yes为某一段插槽的主从挂了,整个集群都挂掉.no为某一段插槽主从挂了,该插槽数据不能使用
>	cluster-require-full-coverage yes
>```
>
>更多参考:[Redis主从复制、哨兵、Cluster三种模式](https://zhuanlan.zhihu.com/p/194143258)
>
>**哈希槽**
>
>````
>一个Redis Cluster包含（0-16384)各哈希槽
>3个节点:A节点(0-5499),B节点(5500-10999),C节点(11000-16383)
>计算方式: slot=CRC16（key）/16384
>````
>
>**集群中执行命令流程**
>
>```
>1.客户端向集群节点发送数据命令
>2.计算键key属于那个槽slot
>3.槽在当前节点直接执行命令
>  槽不在当前节点:节点向客户端返回Redirected(MOVED命令),指引客户端转向至正确的节点,并再次发送要执行的命令
>```
>
>
>
>**Redis Cluster是如何将数据分片的?** 
>
>
>
>

#### 11.三大缓存问题

>1.缓存穿透
>
>2.缓存击穿
>
>3.缓存雪崩



##### 1.缓存穿透

>指访问大量缓存不存在的数据(和不存在的空值),缓存命中率降低了
>
>**解决方案**
>
>1.对数据库中的空值进行缓存,设置较短的过期时间(维护较简单，但是效果不好)
>
>2.使用布隆过滤器(维护复杂，效果很好)
>
>**布隆过滤器**
>
>```
>是一个很长的二进制向量和一系列随机映射函数，用于检索一个元素是否在一个集合中
>优点：
>	空间效率和查询时间都比一般的算法要好的多，增加和查询的时间复杂度为O(N)N为hash函数个数
>缺点：
>	是有一定的误识别率和删除困难
>```
>
>Redis中的布隆过滤器底层是**一个大型位数组（二进制数组）+多个无偏hash函数**
>
>```
>多个hash函数计算一个值的不同hash，并产生多个索引值,将数组上对应的索引位置置为1
>```
>
>

##### 2.缓存击穿

>冷门数据大并发，或者是一个`key`非常热点，有着大并发,当这个key失效的随间，持续的**大并发**就穿破缓存，直接请求数据库，瞬间对数据库的访问压力增大
>
>**解决方案**
>
>1.预先设置热门数据,设置较大的过期时间,实时调整
>
>2.加锁，对第一个进来的请求执行并做缓存,接下来的就命中缓存

##### 3.缓存雪崩

>缓存雪崩 是指在某一个时间段，缓存集中过期失效。此刻无数的请求直接绕开缓存，直接请求数据库
>
>**解决方案**
>
>1.构建多级缓存架构和redis集群
>
>2.分散过期时间
>
>3.限流降级

更多参考[Redis缓存三大问题](https://zhuanlan.zhihu.com/p/140772422)

#### 12.相关问题

>**Redis为什么这么快?**
>
>```
>1.Redis 是纯内存结构的，避免了磁盘 I/O 等耗时操作。
>2.Redis 命令处理的核心模块为单线程，减少了锁竞争，以及频繁创建线程和销毁线程的代价，减少了线程上下文切换的消耗。
>3.采用了 I/O 多路复用机制，大大提升了并发效率。
>```
>
>**Redis为什么是单线程?**
>
>```
>CPU不是redis的瓶颈,不会有太多的计算和逻辑判断,最有可能机器内存和网络带宽
>
>```
>
>**Redis6.0为什么引入了多线程?**
>
>```
>瓶颈在网络I/O模块带来的CPU耗时,引入的多线程用来处理网络I/O部分。
>```
>
>**是否有并发安全问题?**
>
>```
>内存操作，依然是单线程运行的。redis 的多线程部分只是用来处理网络数据的读写和协议解析，执行命令仍然是单线程顺序执行，也就不存在并发安全问题
>```
>
>**如何开启多线程？**
>
>```
>配置文件开启多线程：
>io-thread-do-reads yes
>io-thread 线程数
>```
>
>**如何实现优先级队列？**
>
>```
>使用Zset,是一个有序队列,每个元素member都有一个分数score
>```
>
>**如何实现延迟队列?**
>
>使用Zset，score为当前时间+时间戳
>
>```
>生产者:
># key为队列的名称，score为当前的时间戳+延迟时间，member为消息体
>zadd key score member
>消费者:一直循环从redis的zset队列获取数据
># key为队列的名称，min为0，max为当前的时间戳，limit为单次个数
>zrangebyscore key min max limit
>消费删除:
>zrem key member
>```
>
>



参考[Redis常见面试题](https://cloud.tencent.com/developer/article/2315477)
