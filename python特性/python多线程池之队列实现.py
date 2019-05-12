#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午6:27
##用一个叫做 Queue 的队列来创建线程池

import threading
import time
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def moyu():
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def queue_pool():
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()
    #setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
    # 这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，
    # 就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义
    """  
    使用setDaemon之后，主线程里面如果不写一个死循环那么运行之后主线程把所有子线程start之后主线程就算是结束了他的工作，
    主线程结束之后立马就会把所有子线程kill掉，那么这样有什么意义呢？
    
    
使用setDaemon()和守护线程这方面知识有关， 比如在启动线程前设置thread.setDaemon(True)，就是设置该线程为守护线程，
表示该线程是不重要的,进程退出时不需要等待这个线程执行完成。
这样做的意义在于：避免子线程无限死循环，导致退不出程序，也就是避免楼上说的孤儿进程。

thread.setDaemon（）设置为True, 则设为true的话 则主线程执行完毕后会将子线程回收掉,
设置为false,主进程执行结束时不会回收子线程
setDaemon()说明：
setDaemon() ： 设置此线程是否被主线程守护回收。默认False不回收，需要在 start 方法前调用；
设为True相当于像主线程中注册守护，主线程结束时会将其一并回收。
    """

    for i in range(20):
        queue.put(moyu)
    queue.join()

if __name__ == '__main__':
    queue_pool()