"""
多线程实现方式：
thread:提供了低级别的、原始的线程以及一个简单的锁。
_thread:python3(python2为thread)
threading: 推荐使用,_thread有的，threading都有
ThreadPoolExecutor: 实现线程池

从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，
实现了对threading和multiprocessing的进一步抽象（这里主要关注线程池），不仅可以帮我们自动调度线程
"""

import threading
import _thread
from concurrent.futures import ThreadPoolExecutor
import time

# _thread
"""
try:
   _thread.start_new_thread( print_func, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_func, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")
"""

# threading.Thread
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



class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程(类实现):" + self.name)
        fuck(self.name, self.counter, 10)
        print("退出线程(类实现):" + self.name)


def fuck(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s 开始fuck %s" % (thread_name, time.strftime("%Y-%m-%d %H:%M:%S")))
        counter -= 1


def all_run():
    thread_1 = MyThread(1, "thread_1", 1)
    thread_2 = MyThread(2, "thread_2", 2)
    thread_3 = threading.Thread(target=fuck, args=("线程函数实现", 2, 4))
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


if __name__ == "__main__":
    # all_run()
    pool = ThreadPoolExecutor(20)  # 创建20个的线程池
    for i in range(1, 5):
        # 提交执行函数到线程池，立即返回，不阻塞
        # submit参数是生成器对象,
        task1 = pool.submit(fuck("线程池" + str(i), 2, 3))


"""


# 线程池
"""
四种线程池实现方式
1.from multiprocessing.dummy import Pool as ThreadPool  # 线程池
2.from multiprocessing.pool import ThreadPool  # 线程池，用法无区别，唯一区别这个是线程池
3.from concurrent.futures import ThreadPoolExecutor  # python原生线程池，这个更主流
4.import threadpool  # 线程池，需要 pip install threadpool，很早之前的
5.用一个叫做 Queue 的队列来创建线程池 
"""

from queue import Queue


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


if __name__ == "__main__":
    queue_pool()

    # setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
    # 这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，
    # 就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义
"""  
1.thread.join：
使用join函数，主线程将被阻塞，一直等待被使用了join方法的线程运行完成(可以设置超时时间join(5) )


2.thread.setDaemon：
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

# 三:concurrent.futures.ThreadPoolExecutor
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
    wait,
    ALL_COMPLETED,
    FIRST_COMPLETED,
)
import threading
import time


# 1:ThreadPoolExecutor
# 回调函数
def get_result(future):
    print(future.result())


def Actioin(max, a, b, c):
    total = 0
    print(a + b + c)
    for i in range(max):
        print(threading.current_thread().name + ":" + str(i))
        total += 1
    return total


# 1.创建一个线程池 submit(fn, *args, **kwargs)
pool = ThreadPoolExecutor(max_workers=5)
future_1 = pool.submit(
    Actioin, 10, "yuan", "bingx", "xi"
)  # 提交一个task，并传入参数:传参不要元组，接着往后写，有多少写多少
future_2 = pool.submit(Actioin, 20, "君君", "臣臣", "父父")

# 2.添加回调函数
future_1.add_done_callback(get_result)
future_1.done()  # 判断任务是否结束
future_1.result()  # 获取任务返回的结果：.result()会阻塞当前线程，如果没有指定 timeout 参数，当前线程将一直处于阻塞状态，直到 Future 代表的任务返回
# future_1.cancel()  # 取消任务,如果任务已在线程池中运行,就取消不了
future_1.cancelled()  # 返回 Future 代表的线程任务是否被成功取消。
future_1.running()  # 如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True
future_1.exception(timeout=None)  # 获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None
# 3.等待线程池中的任务执行完后再执行其他线程
wait(
    future_1, return_when=FIRST_COMPLETED
)  # return_when:表示wait返回结果的条件,FIRST_COMPLETED:表示完成第一个任务后就执行主线程

# 4. as_completed 使用as_completed方法一次取出所有任务的结果。
"""
as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务，
就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，先完成的任务会先通知主线程
"""
for future in as_completed([future_1, future_2]):
    message = future.result()
# 关闭线程池
pool.shutdown()

# 2: with
"""由于线程池实现了上下文管理协议（Context Manage Protocol），因此，程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池"""
# a = (10,"1","12","123")
# b = (20,"21","212","2123")
# c = (30,"31","312","3123")
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用map()来启动 3 个线程:元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(Actioin, (10, 30, 90))
    # results = pool.map(Actioin,(a,b,c))  error
