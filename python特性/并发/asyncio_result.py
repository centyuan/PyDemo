import asyncio
import time
# https://dandelioncloud.cn/article/details/1527236399728443394
# 一:
now = lambda: time.time()


async def do_some_work(x):
    print("第二waiting:", x)
    await asyncio.sleep(x)
    return "第二Done after {}s".format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    # return await asyncio.wait(tasks) 那么最外层的run_until_complete将会返回main协程的结果
    return await asyncio.wait(tasks)
    # 2.如果使用的是 asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果
    # return await asyncio.gather(*tasks)
    # 不用return await asyncio.wait(tasks),那么里面获任务结果
    dones,pendings = await asyncio.wait(tasks)
    for task in dones:
        print('结果:',task.result())

start = now()
loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())
for task in done:
    print("Task ret:", task.result())
# 2.
# results = loop.run_until_complete(main())
# for result in results:
#     print("Task ret:", result)

print("Time:", now() - start)

# 二: 协程停止处理
# 先遍历取消事件，停止循环，在重启事件循环，最后在close，不然还会抛出异常

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
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print("Time:", now() - start)

# 三:线程加协程 实现动态添加协程
import asyncio
import time
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))
# 不阻塞
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
# 主线程不会被block
while 1:
    time.sleep(1)
    print('1')
# 阻塞
# new_loop.call_soon_threadsafe(more_work, 6)
# new_loop.call_soon_threadsafe(more_work, 3)
