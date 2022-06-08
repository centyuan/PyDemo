#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-15 下午8:02

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='task_queue')
print('[*] wait for messages. To exit press CTRL+C')

def callback(ch,method,properties,body):
    print('[x] Received %r'%(body))
    print(type(body))
    #time.sleep(body.count('.')) #str.count(' ')
    time.sleep(15)
    print('[x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag) #告诉rabbitMQ已经收到并处理了消息

#使用basic_qos,并设置prefetch_count=1这样告诉RabbitMQ
#再同一时刻，不要发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并且作出了响应。
# 这样，RabbitMQ 就会把消息分发给下一个空闲的工作者（worker）
channel.basic_qos(prefetch_count=1)

channel.basic_consume('task_queue',callback)

channel.start_consuming()