import pika
import sys

# 1.创建连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
credential = pika.PlainCredentials("admin","abc123yuan")
params = pika.ConnectionParameters("43.136.217.222",5672,"/",credential)
connection = pika.BlockingConnection(params)
channel = connection.channel()
# 2.创建一个direct类型的exchange
channel.exchange_declare(exchange='direct_logs',
                         type='direct')
# 3.创建一个queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    print >> sys.stderr, "Usage: %s [pub] [msg] [info] [warning] [error]" % \
                         (sys.argv[0],)
    sys.exit(1)

for severity in severities:
    #绑定多个交换机和队列关系
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body,))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()