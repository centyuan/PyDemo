import threading
import time
from queue import Queue
"""
四种线程池实现方式
1.from multiprocessing.dummy import Pool as ThreadPool  # 线程池
2.from multiprocessing.pool import ThreadPool  # 线程池，用法无区别，唯一区别这个是线程池
3.from concurrent.futures import ThreadPoolExecutor  # python原生线程池，这个更主流
4.import threadpool  # 线程池，需要 pip install threadpool，很早之前的
"""
""" 用一个叫做 Queue 的队列来创建线程池 """


class CustomThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            q_method = self.queue.get()
            q_method()
            self.queue.task_done()


def moyu():
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    time.sleep(3)


def queue_pool():
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()
    for i in range(20):
        queue.put(moyu)
    queue.join()


if __name__ == '__main__':
    queue_pool()

    # setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
    # 这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，
    # 就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义
    """  
1.thread.join
使用join函数，主线程将被阻塞，一直等待被使用了join方法的线程运行完成(可以设置超时join(5) )


2.thread.setDaemon
Python多线程的默认情况（设置线程setDaemon(False)），主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束
比如在启动线程前设置thread.setDaemon(True)，就是设置该线程为守护线程，
表示该线程是不重要的,进程退出时不需要等待这个线程执行完成。
这样做的意义在于：避免子线程无限死循环，导致退不出程序，也就是避免楼上说的孤儿进程。
setDaemon()说明：
setDaemon() ： 设置此线程是否被主线程守护回收。默认False不回收，需要在 start 方法前调用；
设为True相当于像主线程中注册守护，主线程结束时会将其一并回收。

example:
usage:开启守护线程，同时给join设置超时
result:超时未处理完毕的子线程将被直接终止
    """
