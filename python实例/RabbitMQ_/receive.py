#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-9 下午7:59
import  pika
#创建连接

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
#创建通道
channel = connection.channel()
#确认队列是否存在
#使用queue_declare创建一个队列——我们可以运行这个命令很多次，但是只有一个队列会被创建。
channel.queue_declare(queue='hello')

print ('[*] Waiting for messages. To exit press CTRL+C')

#为队列定义回调函数
def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))

#告诉 RabbitMQ 这个回调函数将会从名为 "hello" 的队列中接收消息：
# channel.basic_consume(callback,
#                       queue='hello',
#                       no_ack=True) #no_ack关闭了消息响应
#参数位置变了，修改如下不然报错

channel.basic_consume('hello',callback)
channel.start_consuming()

