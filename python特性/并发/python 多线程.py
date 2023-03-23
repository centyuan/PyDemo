# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-10 上午9:18
"""
1.常用的多线程模块
_thread:python3(python2为thread)
threading 推荐使用
thread提供了低级别的、原始的线程以及一个简单的锁。_thread有的，threading都有，

2.可以使用 ThreadPoolExecutor 来实现线程池
从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，
实现了对threading和multiprocessing的进一步抽象（这里主要关注线程池），不仅可以帮我们自动调度线程

"""

import threading
import _thread
from concurrent.futures import ThreadPoolExecutor
import time

# 方式1._thread.start
"""
try:
   _thread.start_new_thread( print_func, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_func, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")
"""
# 方式2 threading.Thread 建议采用
"""
threading.currentThread() 返回当前线程变量
threading.enumerate() 返回当前存在的所有线程对象的列表
threading.active_count() 返回正在运行的线程数量 = len(threading.enumerate())
threading.current_thread() 返回当前线程对象
threading.get_ident() 返回线程pid
threading.main_thread() 返回主线程对象
run()
start()    # 创建好一个线程对象后，该对象并不会立即执行,除非调用它的start()方法
join()     # 等待至线程中止,对于需要长时间运行的线程或需要一直运行的的后台任务,考虑使用后台线程:Thread(target=countdown, args=(10,), daemon=True)
isAlive() 返回线程是否活动的
getName()返回线程名
setName()设置线程名
"""

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


def all_run():
    thread_1 = MyThread(1, 'thread_1', 1)
    thread_2 = MyThread(2, 'thread_2', 2)
    thread_3 = threading.Thread(target=fuck, args=('线程函数实现', 2, 4))
    print("开始主线程A:")

    thread_1.start()
    thread_2.start()
    thread_3.start()
    # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止- 正常退出或者抛出未处理的异常-或者是可选的超时发生。
    # 主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，阻塞shi调用
    thread_1.join()
    thread_2.join()
    thread_3.join()
    print("退出主线程A")


if __name__ == '__main__':
    # all_run()
    pool = ThreadPoolExecutor(20)  # 创建20个的线程池
    for i in range(1, 5):
        # 提交执行函数到线程池，立即返回，不阻塞
        # submit参数是生成器对象,
        task1 = pool.submit(fuck('线程池' + str(i), 2, 3))

"""
task.done()         # 定某个任务是否完成
task.cancel()       # 用于取消某个任务,该任务没有放入线程池中才能取消成功
task.result()       # result方法可以获取task的执行结果 

as_completed()      # 一次性获取所有结果
all_task = [executor.submit(get_html, (url)) for url in urls]
for future in as_completed(all_task):
    data = future.result()
    print("in main: get page {}s success".format(data))
    
"""
