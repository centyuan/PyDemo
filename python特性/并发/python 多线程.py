# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-10 上午9:18
"""
1.常用的多线程模块
_thread(python2 thread,ps:thread在python2中3中改为_thread)
threading 推荐使用
Queue
thread提供了低级别的、原始的线程以及一个简单的锁。_thread有的，threading都有，

2.可以使用 ThreadPoolExecutor 来实现线程池
"""
import threading
import _thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor #进程池
import time

# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-
# 正常退出或者抛出未处理的异常-或者是可选的超时发生。

# 1._thread.start
'''
try:
   _thread.start_new_thread( print_func, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_func, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")
'''

# 2 threading.Thread
"""
threading.currentThread() 返回当前线程变量
threading.enumerate() 返回一个包含正在运行线程的list
threading.activeCount() 返回正在运行的线程数量 = len(threading.enumerate())
run()
start()
join()
isAlive() 返回线程是否活动的
getName()返回线程名
setName()设置线程名

"""
lock = threading.Lock()
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程(类实现):' + self.name)
        fuck(self.name, self.counter, 10)
        print('退出线程(类实现):' + self.name)


def fuck(thread_name, delay, counter):
    while counter:

        time.sleep(delay)
        print("%s 开始fuck %s" % (thread_name, time.strftime("%Y-%m-%d %H:%M:%S")))
        counter -= 1


def thr_run():
    thread_cent = MyThread(1, '线程类实现cent', 1)
    thread_yuan = MyThread(2, '线程类实现yuan', 2)
    thread3 = threading.Thread(target=fuck, args=('线程函数实现', 2, 4))
    # 开启新线程
    print("开始主线程A")
    thread_cent.start()
    thread_yuan.start()
    thread3.start()
    # 主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行
    #阻塞shi调用
    thread_cent.join()
    thread_yuan.join()
    thread3.join()
    print("退出主线程A")

if __name__ == '__main__':
    thr_run()
    pool = ThreadPoolExecutor(20)  # 创建20个的线程池
    for i in range(1, 5):
        #fuck为线程任务
        pool.submit(fuck('线程' + str(i), 2, 3))
