import pika
# 二:广播模式
# 1.创建连接
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222","5672","/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道channel
channel = connection.channel()
# 3.创建交换机exchange
channel.exchange_declare(exchange="logs",exchange_type="fanout")
# 4.创建queue
channel.queue_declare(queue="logs2_queue")
# 5.绑定交换机和队列
channel.queue_bind(exchange="logs",queue="logs2_queue")
# 6.消费
# 回调函数
def callback(ch,method,properties,body):
    print("回调函数:",body)
channel.basic_consume("logs2_queue",callback,auto_ack=True)
channel.start_consuming()
