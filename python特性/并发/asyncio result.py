# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/21 13:07
#1
import asyncio
import time

now = lambda: time.time()
async def do_some_work(x):
    print("第一waiting:",x)
    await asyncio.sleep(x)
    return "第一Done after {}s".format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    return await asyncio.gather(*tasks)
start = now()
loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
for result in results:
    print("第一Task ret:",result)

print("第一Time:", now()-start)


# 2
now = lambda: time.time()
async def do_some_work(x):
    print("第二waiting:",x)
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
    return await asyncio.wait(tasks)

start = now()
loop = asyncio.get_event_loop()
done,pending = loop.run_until_complete(main())
for task in done:
    print("Task ret:",task.result())
print("Time:", now()-start)


#3 协程停止处理
# 先遍历取消事件，停止循环，在重启事件循环，最后在close，不然还会抛出异常

now = lambda :time.time()
async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

coroutine1 =do_some_work(1)
coroutine2 =do_some_work(2)
coroutine3 =do_some_work(2)

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
print("Time:",now()-start)

#4线程加协程 实现动态添加协程
import asyncio
import time
from threading import Thread

now = lambda :time.time()

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
#阻塞
#new_loop.call_soon_threadsafe(more_work, 6)
#new_loop.call_soon_threadsafe(more_work, 3)



