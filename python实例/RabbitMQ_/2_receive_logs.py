import pika
# 二:广播模式
# 1.创建连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222","5672","/",credential)
connection = pika.BlockingConnection(params)
# 2.创建通道channel
channel = connection.channel()
# 3.创建交换机exchange,durable是否持久化(指交换机会不会随着服务重启造成丢失)
channel.exchange_declare(exchange='logs',exchange_type='fanout',durable=True)  # 广播模式
# 4.创建queue
result = channel.queue_declare(queue='logs_queue')
queue_name = result.method.queue
# 5.绑定交换机和队列
channel.queue_bind(exchange='logs',queue=queue_name)
#channel.queue_bind(exchange='logs',queue=queue_name,routing_key='black')
#routing_key:绑定键
"""
实现多个绑定
for severity in severities:
    channel.queue_bind(exchange='logs',
                       queue=queue_name,
                       routing_key=severity
                       )
"""

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] %r"%(body))

channel.basic_consume(queue_name,callback,auto_ack=True)
channel.start_consuming()


