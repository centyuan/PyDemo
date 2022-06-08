#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-15 下午10:02

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')  # 广播模式

#不提供 queue 参数就可以创建临时队列
result = channel.queue_declare()
queue_name = result.method.queue
#绑定交换机和队列
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

channel.basic_consume(queue_name,callback)
channel.start_consumeing()


