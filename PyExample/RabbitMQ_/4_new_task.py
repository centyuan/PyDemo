import pika
import sys
# 1.创建连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222",5672,"/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道
channel = connection.channel()
message = ' '.join(sys.argv[1:]) or '.new test'
# 3.创建queue
channel.queue_declare(queue='task_queue',durable=True) #durable队列持久化
# 4.发送消息
channel.basic_publish(exchange='', #匿名交换机
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2 #make message persistent 消息持久化
                      )
                      )

print("[x] Sent %r"%(message))