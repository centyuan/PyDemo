import pika
import datetime

# 1.创建连接
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222",5672,"/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道
channel = connection.channel()
# 3.创建死信exchange,queue
channel.exchange_declare(exchange="dead_exchange",exchange_type="topic")
channel.queue_declare(queue="dead_queue",)
channel.queue_bind(queue="dead_queue",exchange="dead_exchange",routing_key="dead_test")
# 4.dead letter转发参数
arguments = {
    "x-dead-letter-exchange":"dead_exchange",
    "x-dead-letter-routing-key":"dead_test",
    "x-message-ttl":10000  # 毫秒ms
}
# 5.辅助ttl,exchange,queue声明
channel.exchange_declare(exchange="ttl_exchange",exchange_type="topic")
channel.queue_declare(queue="ttl_queue",arguments=arguments)
channel.queue_bind(queue="ttl_queue",exchange="ttl_exchange",routing_key="ttl_test")
print("现在时间:",datetime.datetime.now())
channel.basic_publish(exchange="ttl_exchange",routing_key="ttl_test",body="hello world.")
