import pika
import sys
# 二:fanout广播模式
# 1.创建连接
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222","5672","/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道
channel = connection.channel()
# 3.创建交换机 fanout广播模式,所有绑定的queue都能收到消息
channel.exchange_declare(exchange='logs',exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='',body=message)
print(" [x] Sent %r" % (message,))
connection.close()

