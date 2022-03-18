# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/5 15:39

"""
不被操作系统内核管理
协程，又称微线程，是一种用户态的轻量级线程。协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态，
换种说法：进入上一次离开时所处逻辑流的位置，当程序中存在大量不需要CPU的操作时（IO），适用于协程

1:子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销
2:不需要多线程的锁机制，只有一个线程，不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了.
3:协程是一个线程执行，所以想要利用多核CPU，最简单的方法是多进程+协程，这样既充分利用多核，又充分发挥协程的高效率
"""
'''
1、必须在只有一个单线程里实现并发 
2、修改共享数据不需加锁
3、用户程序里自己保存多个控制流的上下文栈 
4、一个协程遇到IO操作自动切换到其它协程
'''
#1:greenlet
#Greenlet（greenlet的执行顺序需要我们手动控制）

from greenlet import greenlet #初级
import time
import gevent
#1 greenlet实现协程
def task_1():
    while True:
        print("--This is task 1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)

def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)

#2 gevent 实现协程
def task_gevent(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep


# asyncio 实现异步协程 （python中使用协程最常用的库就是asyncio）
if __name__ == "__main__":
    # #1 greenlet
    # g1 = greenlet(task_1)  # 定义greenlet对象
    # g2 = greenlet(task_2)
    # g1.switch()  # 切换到g1中运行
    #2 gevent
    g1 = gevent.spawn(task_1, 5)  # 创建协程
    g2 = gevent.spawn(task_1, 5)
    g3 = gevent.spawn(task_1, 5)
    g1.join()  # 等待协程运行完毕
    g2.join()
    g3.join()

