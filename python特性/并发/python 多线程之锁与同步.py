"""
GIL全局解释锁:因为引用计数管理内存,所以某个对象的引用计数不能被两个线程同时增加和减少,或内存泄露:永远不释放,GIL对线程间共享的所有数据结构加锁可以保证引用计数变量的安全性
Python 线程会去主动释放 GIL:这种机制叫间隔式检查（check_interval）,每隔一段时间，Python 解释器就会强制当前线程去释放 GIL，这样别的线程才能有执行的机会
### GIL锁的释放
### 1.协同式多任务处理：IO操作，在较长的或者不确定的时间，没有运行Python代码的需要，线程便会让出GIL；
### 2.抢占式多任务处理：对于CPU密集型的的程序，解释器运行一段时间就会放弃GIL,而不需要经过正在执行代码的线程允许，这样其他线程便能运行。（在python3中，这个时间间隔是15毫秒）

# 控制多线程同步的原语,Locks、RLocks、Semaphores、Events、Conditions和Barriers(python3.2之后引入)，还有Queue,可以继承这些类，实现自己的同步控制原语。
线程同步
"""
# 參考https://www.cnblogs.com/chengd/articles/7770898.html
# 1.threading.Lock()
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000):
        # 获取锁
        # lock.acquire(timeout=10)
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
if __name__ == '__main__':
    # 加锁保证balance一直为0
    t1 = threading.Thread(target=run_thread,args=(10,))
    t2 = threading.Thread(target=run_thread,args=(15,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


# 2.threading.RLock(): RLock允许在同一线程中被多次acquire
threading.RLock()

# 3.threading.Condition()高级的琐
threading.Condition()

# 4.threading.Semaphore():内部管理着一个计数器。调用 acquire() 会使这个计数器 -1，release() 则是+1(可以多次release()，
# threading.BoundedSemaphore
threading.Semaphore(10)

# 5.threding.Event():全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞；如果“Flag”值为True，那么执行event.wait 方法时便不再阻塞。
threading.Event()

"""
# http://c.biancheng.net/view/2620.html
死锁情况：两个线程都执行函数，并获取自己线程锁，获取锁后，调用对方对象的方法(对方方法会获取锁)
如何避免死锁:
1.避免在一个线程里，对多个Lock进行锁定。
2.需要多个Lock锁定时:都按照相同的加锁顺序。
3.使用定时锁:acquire()方法加锁时可指定 timeout 参数, timeout 秒后会自动释放对 Lock 的锁定
4.死锁检测:是一种依靠算法机制来实现的死锁预防机制，它主要是针对那些不可能实现按序加锁，也不能使用定时锁的场景的

"""
