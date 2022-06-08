import pika
import json
import time
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def call_back(ch, method, properties, body):
    print("接收消息: %r" % (body,))


class Rabbitmq_producer(object):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.port = 5672
        self.msg_list = None
        self.rbt_connection()

    def rbt_connection(self):
        hosts = "127.0.0.1"
        host = hosts
        print("连接参数", self.user, self.pwd, self.port, host)
        credential = pika.PlainCredentials(self.user, self.pwd)
        try:
            pid = pika.ConnectionParameters(host, self.port, '/', credential)
            connection = pika.BlockingConnection(pid)
            self.channel = connection.channel()
            self.channel.exchange_declare(exchange='first', exchange_type='fanout')
            self.channel.queue_declare(queue='first_queue')
            self.channel.queue_bind(exchange='first', queue='first_queue')
            print("____________channel:", self.channel)
            return self.channel
        except Exception as e:
            logger.error("connect rabbitmq failed: %s" % e)
            print("连接失败")

    def publish(self, msg_list):
        msg = json.dumps(msg_list)
        print(msg)
        self.channel.basic_publish(exchange='first', routing_key='', body=msg)

    def consume(self):  # 获取数据
        self.channel.basic_consume('first_queue', call_back)
        print("开始消费")
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
        hosts = "127.0.0.1"
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
        self.channel.basic_consume('first_queue', call_back)
        print("开始消费")
        self.channel.start_consuming()


if __name__ == '__main__':
    print("生产者")
    rabbitmq = Rabbitmq_producer("yuan", "yuan")
    rabbitmq.publish(["kevinmitnick"])
    time.sleep(3)
    print("消费者")
    rabbitmq = Rabbitmq_consumer("coolfire", "coolfire")
    rabbitmq.consume()

"""
用户仅能对其所能访问的virtual hosts中的资源进行操作。这里的资源指的是virtual hosts中的exchanges、queues等，操作包括对资源进行配置、写、读。配置权限可创建、删除、资源并修改资源的行为，写权限可向资源发送消息，读权限从资源获取消息。比如：
exchange和queue的declare与delete分别需要exchange和queue上的配置权限
exchange的bind与unbind需要exchange的读写权限
queue的bind与unbind需要queue写权限exchange的读权限
发消息(publish)需exchange的写权限
获取或清除(get、consume、purge)消息需queue的读权限
需要注意的是RabbitMQ会缓存每个connection或channel的权限验证结果、因此权限发生变化后需要重连才能生效。
"""