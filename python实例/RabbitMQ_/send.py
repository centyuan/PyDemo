#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-9 下午7:43

import pika
#创建一个到RabbitMQ服务器的连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
#创建一个名为hello的队列
channel.queue_declare(queue='hello')

#在 RabbitMQ 中，消息是不能直接发送到队列，它需要发送到交换机（exchange）中，
# 它使用一个空字符串来标识。交换机允许我们指定某条消息需要投递到哪个队列。
#routing_key 指定队列的名称
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='to be or not to be!')
print (" [x] Sent 'to be or not to be!'")
connection.close()