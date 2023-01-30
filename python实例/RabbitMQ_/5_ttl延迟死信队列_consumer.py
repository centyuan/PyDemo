import pika
import datetime


def call_back(channel, method, properties, body):
    print("时间:", datetime.datetime.now())
    print("消息:", body)


# 1.创建连接
credential = pika.PlainCredentials("admin", "abc123yuan")
params = pika.ConnectionParameters("43.136.217.222", 5672, "/", credential)
connection = pika.BlockingConnection(params)
# 2.创建通道
channel = connection.channel()
# 3.
channel.exchange_declare(exchange="dead_exchange", exchange_type="topic")
channel.queue_declare(queue="dead_queue")
channel.queue_bind(queue="dead_queue", exchange="dead_exchange", routing_key="dead_test")
# 4.消费死信队列里的消息
channel.basic_consume(on_message_callback=call_back,queue="dead_queue",auto_ack=True)
channel.start_consuming()

