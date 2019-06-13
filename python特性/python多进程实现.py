#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午8:31
import os

from multiprocessing import Process,Pool #多进程

def f(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def fpool(x):
    return x*x

if __name__ =='__main___':
    print('Parent process %s.' % os.getpid())
    p=Process(target=f,args=('centyuan',))#一个执行函数，和函数的参数
    p.start()#创建Process实例，用start启动
    p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    #Pool(number)创建进场池 要启动大量的子进程，可以用进程池的方式批量创建子进程：

    with Pool(5) as p:
        print(p.map(fpool,[1,2,3]))



