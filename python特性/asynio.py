# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 19:39

import time
import asyncio
import threading

"""
asyncio 使用event_loop实现高并发的模块
"""
#1同步代码
def hello_1():
    time.sleep(1)


def run():
    for i in range(5):
        hello_1()
        print("Hello world %s"%time.time())

#2异步代码
#协程coroutine 要用async声明
async def hello_2():
    #await 当前协程任务等待睡眠时间，用于挂起
    #asyncio.sleep(1)看成是一个耗时1秒的IO操作，
    # 在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
    await asyncio.sleep(1)
    print("asyncio hello world %s"%time.time(),threading.currentThread())


if __name__ == "__main__":
    #1.同步
    run()
    #2.异步
    #asyncio.get_event_loop()时会创建事件循环
    loop = asyncio.get_event_loop()
    tasks = [hello_2() for i in range(5)]
    #异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。
    #loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task
    #task.add_done_callback(callback)绑定回调
    loop.run_until_complete(asyncio.wait(tasks)) #asyncio.gatjer(tasks[0],task[1])
    loop.close()