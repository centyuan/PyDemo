#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-15 下午9:53

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()


#创建交换机
#channel.exchange_declare(exchange='logs',type='fanout') 报错
channel.exchange_declare(exchange='logs',exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message
                      )

print(" [x] Sent %r" % (message,))
connection.close()

