#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-15 下午7:56

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

message = ' '.join(sys.argv[1:]) or '.new test'

channel.queue_declare(queue='task_queue',durable=True) #durable队列持久化
channel.basic_publish(exchange='', #匿名交换机
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2 #make message persistent 消息持久化
                      )
                      )

print("[x] Sent %r"%(message))