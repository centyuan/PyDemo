from kafka import KafkaConsumer
import json 


class MyConsumer():
    def __init__(self, bootstrap_servers:str=None,group_id:str=None,partition=None,**kwargs):
        self.consumer = KafkaConsumer(topic,bootstrap_servers=bootstrap_servers,group_id=group_id,**kwargs)

    def consumer(self):
        for message in self.consumer:
            yield {
                "topic":message.topic,
                "partition":message.partition,
                "key":message.key,
                "value":message.value.decode("utf-8")
            }
        
if __name__ == "__main__":
    broker = "10.24.2.2:9092"
    topic = "notify_topic"
    kafka_consumer = MyConsumer(bootstrap_servers=broker,topic=topic)
    for msg in kafka_consumer.recv():
        print("消息:",msg)
