"""
pip install kafka-python
"""
import json 
from kafka import KafkaProducer
from datetime import datetime
from typing import List 
from kafka.errors import kafka_errors

# https://zhuanlan.zhihu.com/p/637683728
#batch_size: 批次大小,默认64kb,生产者将发送到相同分区的多个信息打包为一个批次,为0表示禁用
#linger.ms: 消息停留时间,到这个时间后必须发送
"""
场景1消息需要按顺序发送并且只能在一个partation上:
    retries:重试次数
    max_in_flight_requests_per_connection=1:控制生产者在收到服务器响应之前只能发送一个消息

场景2只关心吞吐量-容许少量消息发送失败，不关注消息顺序
    异步发送+acks=0

场景3需要知道消息是否发送成功,不关注消息顺序
    异步发送+回调
    retries=0 

发送消息:外网或跨网段需要添加advertised.listeners=PLAINTEXT://hostname:9092
外网访问或有代理的都需要配置这个外部地址/代理地址,advertised.listeners 指明客户端通过哪个 ip 可以访问到当前节点
advertised.listeners=PLAINTEXT://outward-nginx:9092

1.从zookeeper拿到partition分区的leader地址
2.将消息发送给leader
"""

class MyProducer():
    def __init__(self, bootstrap_servers:str=None,topic:str=None):
        self.bootstrap_servers = bootstrap_servers if bootstrap_servers else "127.0.0.1:9092"
        self.topic = topic if topic else "notify_topic"
        self.producer = KafkaProducer(
            value_serializer=lambda v:json.dumps(v).encode("utf-8"),
            key_serialzier=lambda v:json.dumps(v).encode("utf-8"),
            api_version=(0,10,1),
            batch_size=0,
        )
    
    # 1.同步发送
    def send_msg(self, msg:str="你好", partition:int=0):
        future = self.producer.send(self.topic, msg, partition=partition)
        # future.success,future.succeded()
        if future.failed():
            print("发送失败")
            raise Exception(f"发送失败:{future.exception}")
        metadata_ = future.get(timeout=30)  # 同步发送,等待消息的信息
        print("消息分区:",metadata_.partition)
        print("消息offset:",metadata_.offset)
    
    # 2.异步发送,不关心消息是否到达
    def asyn_send_msg(self, msg:str="你好", partition:int=0):
        for item in range(5):
            self.producer.send(self.topic, msg, partition=partition)
        self.producer.flush()  # 异步发送,批量提交
    
    # 3.异步发送+回调,消息发送成功会回调
    def asyn_send_msg_callback(self, msg:str="你好",partition:int=0):
        for item in range(5):
            future = self.producer.send(self.topic, msg, partition=partition)
            future.add_callback(self.send_success)
            future.add_errback(self.send_error)

    def send_success(self):
        print("send_success:发送成功")
        return
    
    def send_error(self):
        print("send_error:发送失败")
        return 
    
if __name__ == "__main__":
    broker = "10.24.2.2:9092"
    topic = "notify_topic"
    kafka_pro = MyProducer(bootstrap_servers=broker,topic=topic)
    kafka_pro.send("hello world")