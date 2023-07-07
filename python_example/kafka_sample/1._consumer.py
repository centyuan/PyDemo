import json

from kafka import KafkaConsumer
from kafka.errors import kafka_errors
import traceback
from kafka import KafkaConsumer
import json 

def MyConsumer():
    # 使用group,对于同一个group的成员只有一个消费者实例可以读取数据
    def __init__(self, bootstrap_servers:str=['43.136.217.222:9092'],group_id:str=None,partition=None,**kwargs):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            api_version=(0,10,2),
            # auto_offset_reset='earliest' # 设置偏移量,读取最早消息
            **kwargs)

        # 订阅多个主题
        # self.consumer.subscribe(topics=('test','test0'))
        for message in self.consumer:
            print("%s:%d:%d: key=%s value=%s" % (
                message.topic, message.partition, message.offset, message.key, message.value))
        # # 手动拉取消息
        # while 1:
        #     msg = consumer.poll(timeout_ms=5)
        #     # 手动异步提交offset确保消息可靠消费
        #     consumer.commit(message=msg,asynchronous=True)

if __name__ == "__main__":
    broker = "10.24.2.2:9092"
    topic = "notify_topic"
    kafka_consumer = MyConsumer(bootstrap_servers=broker,topic=topic)
    for msg in kafka_consumer.recv():
        print("消息:",msg)