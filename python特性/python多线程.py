#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-10 上午9:18
#常用的多线程模块
# _thread threading Queue(_thread有的，threading都有，thread在python2中3中改为_thread)
#在 python 中
#可以使用 ThreadPoolExecutor 来实现线程池

import  threading #子类继承的方式实现
import _thread  #try 创建函数except
from concurrent.futures import ThreadPoolExecutor

import  time

#join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-
# 正常退出或者抛出未处理的异常-或者是可选的超时发生。

# _thread.start

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print('开始线程:'+self.name)
        fuck(self.name,self.counter,10)
        print('退出线程:'+self.name)

def fuck(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s 开始fuck %s" %(threadName,time.strftime("%Y-%m-%d %H:%M:%S")))
            counter -=1

thread1=MyThread(1,'cent',1)
thread2=MyThread(2,'yuan',2)
#开启新线程
thread1.start()
thread2.start()
# 等待至线程中止
thread1.join() #主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行
thread2.join()
print ("退出主线程")

if __name__=='__main__':
    pool=ThreadPoolExecutor(20)#创建20个的线程池
    for i in range(1,5):
        pool.submit(fuck('线程'+str(i),2,3))


