#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-10 上午9:18
#常用的多线程模块
# _thread threading Queue(_thread有的，threading都有，thread在python2中3中改为_thread)
import  threading #子类继承的方式实现
import _thread  #try 创建函数except
import  time

#join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-
# 正常退出或者抛出未处理的异常-或者是可选的超时发生。

# _thread.start

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        pass

