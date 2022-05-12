# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 19:39

import time
import asyncio
import threading

"""
python 协程详解
"""
#   https://zhuanlan.zhihu.com/p/104918655
#   1.python2.x yield+send 利用生成器实现协程

def consumer():
    r = ''
    while True:
        # 这时传递的参数会作为yield表达式的值，而r是返回给调用者的值
        n = yield r
        if not n:
            return
        print('[consumer] Consuming n:%s'%n)
        r = '200 ok'
def producer(c):
    #启动生成器
    """\
    第一次调用send时必须是send(None)，否则会报错，之所以为None是因为这时候还没有一个yield表达式可以用来赋值。
    https://www.cnblogs.com/ellisonzhang/p/10273843.html
    """
    # send(msg)与next()的区别在于send可以传递参数给yield表达式,这时传递的参数会作为yield表达式的值
    # 第一次调用时必须先next()或send(None)
    c.send(None)
    n = 0
    while n <5:
        n = n+1
        print('[producer] producing %s '%n)
        r = c.send(n)
        print('[producer] consumer return:%s'%r)
    c.close()
if __name__ == "__main__":
    c = consumer()
    producer(c)

#   2. python3.4 asyncio+yield from asyncio实现协程

# @asyncio.coroutine把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行
@asyncio.coroutine
def test(i):
    print('test_start',i)
    """
    把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
    """
    r = yield from asyncio.sleep(1)
    print('test_end',i)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

"""
@asyncio.coroutine
def wget(host):
    print("wget %s"%host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

@asyncio.coroutine把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行。
test()会首先打印出test_1，然后yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），
然后接着执行下一行语句。
把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

"""

#   3. asyncio +async/await
async def test(i):
    print('test_start_',i)
    await asyncio.sleep(1)
    print('test_end_', i)
    # 加上await后会把控制权交给主事件循环，在休眠（IO操作）结束后恢复这个协程
    # asyncio.sleep(1)模拟IO操作，这样的休眠不会阻塞事件循环
    # 在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行


if __name__ == '__main__':
    # asyncio.get_event_loop()时会创建事件循环
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    # loop.run_until_complete 阻塞调用
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    # 异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。
    # # task = asyncio.ensure_future(coroutine)
    # # 将task加入事件循环
    # # loop.run_until_complete(task)
    # loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task
    """
    绑定回调函数结果
    def callback(future):
        print("callback:"future.result())
    task = loop.create_task(coroutine)
    task.add_done_callback(callback) #绑定回调
    loop.run_until_complete(task)
    print(task.result()) #
    """


# 4. gevent(greenlet需要人工切换) 遇到耗时的操作，自动切换协程
import gevent
from gevent import monkey;monkey.patch_all(thread=False)

def test(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1) #交出控制权，交替运行
        '''
        当然在实际的代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时gevent会自动完成，
        所以gevent需要将Python自带的一些标准库的运行方式由阻塞式调用变为协作式运行
        这一过程在启动时通过monkey patch完成：
        '''

if __name__ == '__main__':
    gevent.joinall(
        gevent.spawn(test,'http://httpbin.org/ip'),
        gevent.spawn(test,'http://httpbin.org/uuid'),
        gevent.spawn(test,'http://httpbin.org/user-agent')
    )

