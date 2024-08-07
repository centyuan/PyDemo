#### 基础概念

> **Producer: **Producer 即生产者，消息的产生者，是消息的入口
>
> **Broker:**  Broker 是 kafka 一个实例，每个服务器上有一个或多个 kafka 的实例，简单的理解就是一台 kafka 服务器，kafka cluster表示集群的意思
>
> **Topic:**  消息的主题，可以理解为消息队列，kafka的数据就保存在topic。在每个 broker 上都可以创建多个 topic
>
> **Partition:**  Topic的分区，每个 topic 可以有多个分区，分区的作用是做负载，提高 kafka 的吞吐量。同一个 topic 在不同的分区的数据是不重复的，partition 的表现形式就是一个一个的文件夹,每个Partition都是一个有序队列
>
> **Replication:**  每一个分区都有多个副本，副本的作用是做备胎，主分区（Leader）会将数据同步到从分区（Follower）。当主分区（Leader）故障的时候会选择一个备胎（Follower）上位，成为 Leader。在kafka中默认副本的最大数量是10个，且副本的数量不能大于Broker的数量，follower和leader绝对是在不同的机器，同一机器对同一个分区也只可能存放一个副本
>
> **Message:** 每一条发送的消息主体
>
> **Consumer:** 消费者，即消息的消费方，是消息的出口,在实际的应用中，建议消费者组的consumer的数量与partition的数量保持一致
>
> **Consumer Group:**  可以将多个消费组组成一个消费者组，在 kafka 的设计中同一个分区的数据只能被消费者组中的某一个消费者消费。同一个消费者组的消费者可以消费同一个topic的不同分区的数据，这也是为了提高kafka的吞吐量
>
> **Zookeeper:** kafka 集群依赖 zookeeper 来保存集群的的元信息，来保证系统的可用性

https://zhuanlan.zhihu.com/p/442468709
https://juejin.cn/post/7238604003599695928

#### 基本命令

```
#1.配置内网ip vim config/server.properties
listeners=PLAINTEXT://10.0.0.11::9092
#2.配置外网连接
advertised.listeners=PLAINTEXT:ip:9092
#3.后台运行
nohup kafka-server-start.sh config/server.properties 2>&1 &
#4.添加环境变量
vim ~/.bashrc
export KAFKA_HOME=/home/lighthouse/kafka_2.12-3.3.2
export PATH=$KAFKA_HOME/bin:$PATH
#5.查看所有topics
kafka-topics.sh --list --bootstrap-server 43.136.217.222:9092
#6.创建topics
kafka-topics.sh --bootstrap-server 43.136.217.222:9092 --create --topic web --replication-factor 1 --partitions 3
#7.查看某个topic状态
kafka-topics.sh --describe --topic web --bootstrap-server 43.136.217.222:9092
#8.查看消费组
kafka-consumer-groups.sh --list --bootstrap-server 43.136.217.222:9092
#9.查看生产与消费情况
kafka-consumer-groups.sh --describe --bootstrap-server 43.136.217.222:9092
#10.发送消息
kafka-console-producer.sh --broker-list 43.136.217.222:9092 --topic web
#11.消费,from-beginning消费之前的消息
kafka-console-consumer.sh --topic web --bootstrap-server 43.136.217.222:9092 --from-beginning
#12.消费多个topic
kafka-console-consumer.sh --whitelist "web|quick_demo" --bootstrap-server 43.136.217.222:9092
#13.单播消费,一条消息只能被某一个消费者消费
分别在两个客户端执行
kafka-console-consumer.sh --bootstrap-server 43.136.217.222:9092 --consumer-property group.id=testGroup --topic web
#14.多播消费,一条消费能被多个消费者消费,类似publish-subscribe模式
保证消费者属于不同的消费组
kafka-console-consumer.sh --bootstrap-server 43.136.217.222:9092 --consumer-property group.id=testGroup2 --topic web
```

#### Partition分区

> `leader-follower:`
>
> 生产者在向某个主题发送消息时，会根据分配策略将消息发送到对应的分区
> kafka保证同一个分区内的数据是有序的，我们也可以认为一个分区就是一个有序的消息队列
> 每个主题的某一个分区只能被同一个消费组下的其中一个消费者消费，因此我们可以说分区是消费并行度的基本单位。从消费者的角度讲，我们订阅消费了一个主题，也就订阅了该主题的所有分区

#### Kafka消息队列模式

> **一对一**:
>
> 消费者主动拉取数据，消息收到后消息清除
>
> `Producer -> Mesage Queue -> Consumer
>
> **一对多(发布/订阅模式)**
>
> 消息生产者（发布）将消息发布到 topic 中，同时有多个消息消费者（订阅）消费该消息。和点对点方式不同，发布到 topic 中的消息会被所有订阅者消费

#### 消息可靠生产和可靠消费

**可靠生产**(确认+重试)

>确认: send之后判断结果, Kafka 生产者(Producer) 使用 `send` 方法发送消息实际上是异步的操作，我们可以通过 `get()`方法获取调用结果，但是这样也让它变为了同步操作,采用为其添加回调函数的形式
>
>重试: 

**可靠消费**

> 每个分区在同一时间只被一个 consumer 消费，通每个分区被消费的消息在日志中的位置仅仅是一个简单的整数：offset，通过offset来跟踪消费状态
>
> 手动提交偏移量offset+重试+死信队列
> 手动提交偏移量回导致重复消费



#### 如何保证消息的顺序消费

> - 1 个 Topic 只对应一个 Partition
> - （推荐）发送消息的时候指定 key/Partition。



####  如何保证消息不重复消费

**kafka 出现消息重复消费的原因：**

- 服务端侧已经消费的数据没有成功提交 offset（根本原因）。
- Kafka 侧 由于服务端处理业务时间长或者网络链接等等原因让 Kafka 认为服务假死，触发了分区 rebalance。

**解决方案：**

- 消费消息服务做幂等校验，比如 Redis 的 set、MySQL 的主键等天然的幂等功能。这种方法最有效。

- 将 

  `enable.auto.commit`

   参数设置为 false，关闭自动提交，开发者在代码中手动提交 offset。那么这里会有个问题：

  什么时候提交 offset 合适？

  - 处理完消息再提交：依旧有消息重复消费的风险，和自动提交一样
  - 拉取到消息即提交：会有消息丢失的风险。允许消息延时的场景，一般会采用这种方式。然后，通过定时任务在业务不繁忙（比如凌晨）的时候做数据兜底



#### kafka如何将数据写入到对应的分区

1.send指定的分区
2.没有指定分区,则根据key的hash出一个分区
3.没有指定也没有key,则会轮询出一个分区

> `发送消息的方法`
> ack机制：
>
> ```
> 0:立即发送,不等待ack,1:leader收到,-1:producer等ISR中所有的fllower都确认收到数据
> ```
>
> 1.立即发送(不care消息是否成功发送,大部分情况下会成功,producer会自动重试)
> 2.同步发送(通过send方法发送消息,并返回Future对象,get()方法会等待Future对象，看send()方法是否成功)
> 3.异步发送(通过有回调函数的send发送消息,当producer收到Kafka broker的response会触发回调函数)
>
> `kafka消费模式(客户端处理消息和提交反馈两个动作不是原子性)`
>
> **数据传输的事务定义:**
>
> 1.最多一次(客户端收到消息前自动提交反馈了)
> 2.最少一次(客户端处理消息提交反馈,提交反馈时服务可能挂掉,kafka认为消息未被消费,产生消息重复推送)
> 3.正好一次(保证消息处理和提交反馈在同一个事务中,既有原子性)

#### 副本同步策略

> 1.半数以上完成同步，就发送 ack
>
> ```
> 延迟低,选取新的 leader 时，容忍 n 台节点的故障，需要 2n+1 个副本
> ```
>
> 2.全部完成同步，就发送 ack
>
> ```
> 延迟高,选取新的 leader 时，容忍 n 台节点的故障，需要 n+1 个副本
> ```
>
> kafka 采用第二种方案后，可能会出县一个问题：leader 收到数据后。所有的 follower 都开始同步数据，但是某个 follower 因为故障，迟迟不能与 leader 进行同步，那么 leader 就要一直等下去，直到它完成同步，才能发送 ack.
>
> ` 为了解决这个问题，leader 维护了一个动态的 in-sync replica（ISA）`
>
> ```
> isr:In-Sync Replicas isr 是一个副本的列表，里面存储的都是能跟leader 数据一致的副本
> ```

#### kafka 为什么那么快

> - 顺序读写: 由于现代的操作系统提供了预读和写技术，磁盘的顺序写大多数情况下比随机写内存还要快。
> - 零拷技术(Zero-copy): 减少拷贝次数
> - 批量处理: Batching of Messages ,合并小的请求，然后以流的方式进行交互，直顶网络上限。
> - Pull 拉模式 使用拉模式进行消息的获取消费，与消费端处理能力相符

#### 消息丢失/重复消费消息积压

[kafka的消息丢失、重复消费、消息积压等线上问题汇总及优化](https://blog.csdn.net/qq_45076180/article/details/111561984)

#### Other

> kafka.errors.kafkaTimeoutError:KafkaTimeoutError:Batch for TopicPartition(topic="notifyCenter_topic",partition=0) containing 1 record(s) expired:30 seconds have passed since last append
>
> 可以正常后去kafka topic信息
> 发送消息时报这个错,原因是和kafka连接使用了代理，在发送消息时，拿到具体的节点地址不能发送，需要改成代理才行
> kafka对跨网络的访问有个专门的参数:
> advertised.listeners=PLAINTEXT://hostname:9092
> 这个参数配置了,默认返回给生产者或消费者的就是这个参数的内容
