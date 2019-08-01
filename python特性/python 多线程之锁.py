#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-3 下午5:03

import  time,threading

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
        finally: #无论是否有异常都将执行
            #改完之后释放锁
            lock.release()
if __name__=="__main__":
    t1=threading.Thread(target=run_thread,args=(5,))
    t2=threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)