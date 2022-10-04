"""
GIL:全局解释器锁：和内存管理的引用计数有关，GIL不能绝对保证线程的安全
Python 线程会去主动释放 GIL:这种机制叫间隔式检查（check_interval）
：每隔一段时间，Python 解释器就会强制当前线程去释放 GIL，这样别的线程才能有执行的机会



# http://c.biancheng.net/view/2620.html
死锁情况：两个线程都执行函数，并获取自己线程锁，获取锁后，调用对方对象的方法(对方方法会获取锁)
如何避免死锁:
1.避免在一个线程里，对多个Lock进行锁定。
2.需要斗个Lock锁定时:都按照相同的加锁顺序。
3.使用定时锁:acquire()方法加锁时可指定 timeout 参数, timeout 秒后会自动释放对 Lock 的锁定
4.死锁检测:是一种依靠算法机制来实现的死锁预防机制，它主要是针对那些不可能实现按序加锁，也不能使用定时锁的场景的


# 控制多线程同步的原语,Locks、RLocks、Semaphores、Events、Conditions和Barriers，还有Queue,你也可以继承这些类，实现自己的同步控制原语。
线程同步
1.加锁:threading.Lock()
2.concurrent.futures.ThreadPoolExecutor 实现了线程同步
3.

"""