import asyncio
import time

# https://dandelioncloud.cn/article/details/1527236399728443394
"""
有2种方案可以获取返回值
1:可通过调用 task.result() 方法来获取协程的返回值，
但是只有运行完毕后才能获取，若没有运行完毕，result()方法不会阻塞去等待结果，
而是抛出 asyncio.InvalidStateError 错误

2:通过add_done_callback()回调
https://zhuanlan.zhihu.com/p/59621713
"""
# 一:协程嵌套

now = lambda: time.time()


async def do_some_work(x):
    print("协程嵌套waiting:", x)
    await asyncio.sleep(x)
    return "协程嵌套Done after {}s".format(x)


# 1.main处理结果,性能最差
async def main():
    print('main1-----------')
    coroutine1, coroutine2, coroutine3 = do_some_work(1), do_some_work(2), do_some_work(4)
    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]
    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print('结果:', task.result())


start = now()
loop = asyncio.get_event_loop()
# 单个coroutine会被封装成task
loop.run_until_complete(main())
print('time cost: ', now() - start)


# 2.await
async def main():
    print('main2-----------')
    coroutine1, coroutine2, coroutine3 = do_some_work(1), do_some_work(2), do_some_work(3)
    # 不在main处理结果,直接返回await的内容，那么最外层的run_until_complete将会返回main协程的结果
    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]
    return await asyncio.wait(tasks)


start = now()
loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())
for task in done:
    print("Task ret:", task.result())
print('time cost:', now() - start)


# 3.gather()

async def main():
    print('main3-----------')
    coroutine1, coroutine2, coroutine3 = do_some_work(1), do_some_work(2), do_some_work(3)
    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]
    # 使用的是 asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果
    return await asyncio.gather(*tasks)


start = now()
loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
for result in results:
    print('Task ret:', result)
print("Time:", now() - start)

# 二: 协程停止处理 future状态:Pending,Running,Done,Cancelled
# 先遍历取消事件，停止循环，在重启事件循环，最后在close，不然还会抛出异常
print('协程停止处理-----------')
now = lambda: time.time()


async def do_some_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(2)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]
start = now()
loop = asyncio.get_event_loop()
# 启动事件循环后,ctrl+c会触发KeyBorardInterrupt，循环取消task
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    # stop之后,在开启run_forever(),最后在close
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print("Time:", now() - start)

# 三:线程加协程 实现动态添加协程到事件循环
import asyncio
import time
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print('动态注册协程:Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('动态注册协程:Done after {}s'.format(x))


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


start = now()
# 当前线程创建事件循环,新线程启动事件循环
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))
# 使用协程
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
# 使用函数
# new_loop.call_soon_threadsafe(more_work, 6)
# new_loop.call_soon_threadsafe(more_work, 4)

# call_soon():让asyncio直接传入函数,不用async定义个协程
# call_soon_threadsafe和call_soon一样，会考虑线程安全