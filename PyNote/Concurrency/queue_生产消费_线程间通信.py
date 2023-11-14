"""
question:需要在多个线程之间安全地交换信息或数据
answer:
从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素
Queue对象已经包含了必要的锁，所有可以通过它在多线程间安全地共享数据。

"""
import time
import threading
import random
from queue import Queue


class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        random_int = random.randint(0, 100)
        self.queue.put(random_int)
        print('producer add {}:'.format(random_int))
        time.sleep(random.random())


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        get_int = self.queue.get()
        print('consumer lose {}:'.format(get_int))
        time.sleep(random.random())


if __name__ == "__main__":
    queue = Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
