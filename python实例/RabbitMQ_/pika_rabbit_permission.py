import pika
import json
import time
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

"RabbitMQ默认提供了一个Exchange，名字是空字符串，类型是Direct，绑定到所有的Queue（每一个Queue和这个无名Exchange之间的Binding Key是Queue的名字）。所以，有时候我们感觉不需要交换器也可以发送和接收消息，但是实际上是使用了RabbitMQ默认提供的Exchange"
'''
kombu > pika
kafka > rabbitMQ 
https://mp.weixin.qq.com/s/RzxiXBQk3zjHt9PVI3JSQw
'''

def call_back(ch, method, properties, body):
    print("接收消息: %r" % (body,))
    time.sleep(2)
    # 手动消息确认
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    # 或者修改 channel.basic_consume(callback,queue=queue_name,auto_ack=True)



class Rabbitmq_producer(object):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.port = 5672
        self.msg_list = None
        self.rbt_connection()

    def rbt_connection(self):
        hosts = "43.136.217.222"
        host = hosts
        print("连接参数", self.user, self.pwd, self.port, host)
        credential = pika.PlainCredentials(self.user, self.pwd)
        try:
            # 1.配置连接参数及认证
            pid = pika.ConnectionParameters(host, self.port, '/', credential)
            # 2.创建连接
            connection = pika.BlockingConnection(pid)
            # 3.创建channel通道
            self.channel = connection.channel()
            # self.channel.exchange_declare(exchange='first', exchange_type='fanout',auto_delete=False)
            # 4.创建交换机exchange,参数说明:durable是否持久化,auto_delete是否自动删除
            self.channel.exchange_declare(exchange='first', exchange_type='topic',auto_delete=False)
            # 5.创建队列queue
            self.channel.queue_declare(queue='first_queue',auto_delete=False)
            # 6.绑定exchange和queue
            self.channel.queue_bind(exchange='first', queue='first_queue')
            print("____________channel:", self.channel)
            return self.channel
        except Exception as e:
            logger.error("connect rabbitmq failed: %s" % e)
            print("连接失败")

    # def rbt_connection(self):
    #
    #     queue = str('queue')
    #     RABBITMQ_USERNAME = "hc"
    #     RABBITMQ_PASSWORD = "n7pzv8k58re6"
    #     RABBITMQ_HOST = "192.168.8.170"
    #     RABBITMQ_PORT = "5672"
    #     RABBITMQ_VHOST = "vhost_hc"
    #     credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    #     connection = pika.BlockingConnection(pika.ConnectionParameters(
    #         RABBITMQ_HOST,RABBITMQ_PORT, RABBITMQ_VHOST, credentials))
    #     channel = connection.channel()
    #
    #     print('channel', channel)
    #     # 声明'queue'
        #     channel.exchange_declare(exchange='screen_message', exchange_type='fanout')
    #     channel.basic_publish(exchange='screen_message',
    #                           routing_key=str(queue),
    #                           body=json.dumps({"xx":1234567}))
    #     print()
    #     connection.close()


    def publish(self, msg_list):
        msg = json.dumps(msg_list)
        print(msg)
        self.channel.basic_publish(exchange='screen_message', routing_key='', body=msg)


    def consume(self):  # 获取数据
        # 自动确认  auto_ack=True
        # 手动确认  channel.basic_ack(delivery_tag=method.delivery_tag)
        self.channel.basic_consume('first_queue', call_back,auto_ack=True)
        print("生产者开始消费")
        self.channel.start_consuming()


class Rabbitmq_consumer(object):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.port = 5672
        self.msg_list = None
        self.rbt_connection()

    def rbt_connection(self):
        # 从配置文件中获取数据
        hosts = "43.136.217.222"
        host = hosts
        print("连接参数", self.user, self.pwd, self.port, host)
        credential = pika.PlainCredentials(self.user, self.pwd)
        try:
            pid = pika.ConnectionParameters(host, self.port, '/', credential)
            connection = pika.BlockingConnection(pid)
            self.channel = connection.channel()
            self.channel.exchange_declare(exchange='first2', exchange_type='fanout')
            self.channel.queue_declare(queue='first_queue2')
            self.channel.queue_bind(exchange='first2', queue='first_queue2')
            print("____________channel:", self.channel)
            return self.channel
        except Exception as e:
            logger.error("rabbitmq连接失败: %s" % e)
            print("连接失败")


    def publish(self, msg_list):
        msg = json.dumps(msg_list)
        print(msg)
        self.channel.basic_publish(exchange='first', routing_key='', body=msg)


    def consume(self):  # 获取数据
        self.channel.basic_consume('first_queue', call_back,auto_ack=True)
        # auto_ack False 需手动确认
        print("消费者开始消费")
        self.channel.start_consuming()
        print('消费确认')
        # self.channel.basic_ack()
        # self.channel.tx_rollback()
        # self.channel.close()  # 消费者会hang住，监听到有值就调用callback


if __name__ == '__main__':
    print("生产者")
    # rabbitmq = Rabbitmq_producer("hc", "n7pzv8k58re6")
    rabbitmq = Rabbitmq_producer("admin", "abc123yuan")
    rabbitmq.publish(["123"])
    time.sleep(3)
    # print("消费者")
    # rabbitmq = Rabbitmq_consumer("hc", "n7pzv8k58re6")
    # rabbitmq.consume()

"""
用户仅能对其所能访问的virtual hosts中的资源进行操作。这里的资源指的是virtual hosts中的exchanges、queues等，
操作包括对资源进行配置、写、读。配置权限可创建、删除、资源并修改资源的行为，写权限可向资源发送消息，读权限从资源获取消息。比如：
exchange和queue的declare与delete分别需要exchange和queue上的配置权限
exchange的bind与unbind需要exchange的读写权限
queue的bind与unbind需要queue写权限exchange的读权限
发消息(publish)需exchange的写权限
获取或清除(get、consume、purge)消息需queue的读权限
需要注意的是RabbitMQ会缓存每个connection或channel的权限验证结果、因此权限发生变化后需要重连才能生效。

Exchange:
durable ： 为true，声明exchange是持久化的，当RabbitMQ崩溃了重启后exchange仍然存在；
autoDelete ： 当该exchange所有的队列都被unbind之后，该exchange自动被删除；

Queue :
durable : 为true，声明 queue 是持久化的，当RabbitMQ崩溃重启后 queue 仍然存在；
exclusive： 为true，声明该 queue 为排他队列，如果一个队列被声明为排他队列，该队列仅对首次声明它的连接可见，并在连接断开时自动删除该 queue，也就是当 connection 断开后，该 queue 就会被删除；
autoDelete ： 为true，当所有订阅了该 queue 的 consumer 从RabbitMQ断开后就会删除该queue，或者是当 connection 断开后，该 queue 就会被删除，与 exclusive 不同的是，如果一开始就没有 consumer 连接到该 queue，那么该 queue 将不会被删除；
https://www.jianshu.com/p/4be924178248
"""