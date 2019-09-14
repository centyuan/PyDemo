#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-3 下午5:03

import  time,threading
"""
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间

优缺点：锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，
包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，
并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""
balance=0
lock=threading.Lock() #创建一个锁

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
    #如果不加锁,多线程执行多次后,总会出现balance不为0的情况

def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
          change_it(n)
        finally:
            #无论是否有异常都将执行,改完之后都要释放锁
            # 否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
            # 所以我们用try...finally来确保锁一定会被释放。
            lock.release()

if __name__=="__main__":
    t1=threading.Thread(target=run_thread,args=(5,))
    t2=threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)