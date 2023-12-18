"""
python协程(Coroutine)
1.认为线程是轻量级的进程,协程理解为轻量级线程,即微线程
2.协程可以再执行函数A时可以中断后去执行函数B
3.执行效率高,子程序(函数)切换,没有切换线程的开销

event_loop事件循环:注册到事件循环上,开启后,依次执行相应的协程函数,支持注册Future和Task2种类型的对象
coroutine:协程对象,async定义的函数,返回一个协程对象,函数的执行交给event_loop
task任务:一个协程对象是一个原生可以挂起的函数,任务是进一步封装,包含任务各种状态
future:代表将来执行或没有执行的任务的结果,和task没有本质的区别
(future是协程的封装,提供了任务回调/取消/设置任务结果等)
(task是future的子类,再一次封装,实际开发中不需要操作future这种底层对象,而是task)
async:python3.5后用于定义协程
await:执行遇到await后,会挂起当前执行函数,针对耗时的操作
await后面为可等待对象(Future,task,另一个协程)

https://www.cnblogs.com/traditional/tag/%E6%B7%B1%E5%BA%A6%E8%A7%A3%E5%AF%86%20asyncio/

使用uvloop代替asyncio默认事件循环
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
使得任何对 asyncio.get_event_loop() 的调用都将返回一个 uvloop 的实例
"""
import asyncio

# 实现协程的几种方式 https://zhuanlan.zhihu.com/p/104918655
"""
python2.x yield+sened 利用生成器实现协程
python3.4 asyncio+yield from asyncio实现协程
python3.5 asyncio +async/await
第三方模块: greenlet/gevent

真正运行协程
acyncio.run(main())
await main()


"""
# 1.python2.x yield+send 利用生成器实现协程
def consumer():
    r = ''
    while True:
        # 这时传递的参数会作为yield表达式的值，而r是返回给调用者的值
        n = yield r
        if not n:
            return
        print('[consumer] Consuming n:%s' % n)
        r = '200 ok'


def producer(c):
    # 启动生成器
    """\
    第一次调用send时必须是send(None)，否则会报错，之所以为None是因为这时候还没有一个yield表达式可以用来赋值。
    https://www.cnblogs.com/ellisonzhang/p/10273843.html
    """
    # send(msg)与next()的区别在于send可以传递参数给yield表达式,这时传递的参数会作为yield表达式的值
    # 第一次调用时必须先next()或send(None)
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[producer] producing %s ' % n)
        r = c.send(n)
        print('[producer] consumer return:%s' % r)
    c.close()


if __name__ == "__main__":
    c = consumer()
    producer(c)


#   2. python3.4 asyncio+yield from asyncio实现协程

# @asyncio.coroutine把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行
@asyncio.coroutine
def test(i):
    print('test_start', i)
    """
    把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
    """
    yield from asyncio.sleep(1)
    print('test_end', i)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    coroutines = tasks 
    loop.run_until_complete(asyncio.wait(coroutines))
    loop.close()


#   3.python3.5 asyncio +async/await

async def test(i):
    print('test_start_', i)
    await asyncio.sleep(i)
    print('test_end_', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    coroutines = tasks 
    loop.run_until_complete(asyncio.wait(coroutines))
    loop.close()

