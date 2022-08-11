# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 13:20

import time
import threading
import random
from queue import Queue

class Producer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        random_int = random.randint(0,100)
        self.queue.put(random_int)
        print('producer add {}:'.format(random_int))
        time.sleep(random.random())

class Consumer(threading.Thread):
    def __init__(self,queue):
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