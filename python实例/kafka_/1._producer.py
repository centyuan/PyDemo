from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json


def producer_demo():
    # 1.发送json格式数据
    producer = KafkaProducer(
        bootstrap_servers=['43.136.217.222:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode()
    )
    # 2.发送三条消息
    for i in range(0, 3):
        # key,同一个key值,会被送至同一个分区,partition,向分区1发送消息
        # 会创建kafka_demo主题
        # 1.同步发送
        # future = producer.send('kafka_demo', {'key1': 'value1'}).add_callback().add_errback() # 添加回调函数
        future = producer.send('kafka_demo', {'key1': 'value1'})
        print("send{}".format(str(i)))
        try:
            # 监控是否发送成功,ack确认,消息可靠生产
            record_metadata = future.get(timeout=10)
            print("主题topic:",record_metadata.topic)
            print("分区partition:",record_metadata.partition)
            print("偏移量offset:",record_metadata.offset)
        except kafka_errors:
            # 将异常传播轨迹信息转换成字符串
            traceback.format_exc()


if __name__ == '__main__':
    producer_demo()
