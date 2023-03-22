# 一:简单模式
import pika

# 1.创建连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222","5672","/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道
channel = connection.channel()
# 3.使用queue_declare创建一个队列——我们可以运行这个命令很多次，但是只有一个队列会被创建。
channel.queue_declare(queue='hello')
print('[*] Waiting for messages. To exit press CTRL+C')
# 4.为队列定义回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))


# 告诉 RabbitMQ 这个回调函数将会从名为 "hello" 的队列中接收消息：
# no_ack关闭了消息响应
# 参数位置变了，修改如下不然报错
# 5.开始消费
channel.basic_consume('hello', callback)
channel.start_consuming()
