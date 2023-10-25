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
# 一:协程嵌套三种处理结果方式

now = lambda: time.time()


async def do_some_work(x):
    print("协程嵌套waiting:", x)
    await asyncio.sleep(x)
    return "协程嵌套Done after {}s".format(x)


# 1.main处理结果
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



# 四:asyncio并发的正确/错误姿势
# https://zhuanlan.zhihu.com/p/72887901
# https://zhuanlan.zhihu.com/p/73568282

import time
import asyncio


async def do1():
    print("do1:Starting")
    await asyncio.sleep(1)
    print("do1:Ending")
    return "do1"

async def do3():
    print("do3:Starting")
    await asyncio.sleep(3)
    print("do3:Ending")
    return "do3"

async def main1():
    # Way1.gather并发执行
    return_1,return_3 = await asyncio.gather(do1(),do3())  # gather按照顺序返回
    # Way2.asyncio.ensure_future或loop.create_task或asyncio.create_task(python3.7新增高阶接口 asyncio.run())
    # task1 = asyncio.create_task(do1())
    # task3 = asyncio.create_task(do3())
    # await task1
    # await task3
    # # Way3.错误不能并发
    # await do1()
    # await do3()

### asyncio.gather和asyncio.wait区别
### aysncio.ensure_future和loop.create_task和asyncio.create_task
async def main3():
    # Way1.gather并发执行
    return_1,return_3 = await asyncio.gather(do1(),do3())  # gather按照顺序返回函数返回值
    done,pending = await asyncio.wait(do1(),do3())  # wait返回完成任务列表和等待完成任务的列表 
    # 默认情况下,wait会等全部任务执行完成,所以pending默认是空的
    # 参数返回时机:return_when(ALL_COMPLETED/FIRST_COMPLETED/FIRST_EXCEPTION)
    # Way2.asyncio.ensure_future或loop.create_task或asyncio.create_task接受的参数是一个协程(python3.7新增高阶接口 asyncio.run())
    # task1 = asyncio.create_task(do1())      
    # task3 = asyncio.create_task(do3())
    # await task1
    # await task3
    # # Way3.错误不能并发
    # await do1()
    # await do3()

async def main():
    await main1()
    await main3()
def perf_(func):
    print("*"*10) 
    start = time.perf_counter()
    asyncio.run(func())
    print(f"{func.__name__}花费:{time.perf_counter()-start}")


# asyncio.shield():屏蔽取消操作
if __name__ =="__main__":
    # asyncio.run(main())
    asyncio.run(main1())  # 3.7的新增高阶接口,隐式创建loop去执行task
    perf_(main)


# 五:aysncio.get_event_loop和asyncio.new_event_loop和asyncio.set_event_loop

主线程:get_event_loop会创建一个event loop,并且多次调用始终返回该loop
其他线程:get_event_loop会报错,正确使用是loop = asyncio.new_event_loop创建一个本地线程循环 asyncio.set_event_loop(loop)



# 六:执行普通方法 cal_soon(即刻执行),call_at(),call_later(指定时间之后执行)

def call_back(time_sleep):
    print(f"sleep {time_sleep} success")
def stop_loop(loop):
    loop.stop()
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_soon(call_back, 2) # 即刻执行
    loop.call_later(2, call_back, 2) # 
    loop.call_soon(stop_loop, loop)
    loop.run_forever()


# 七：多线程,loop遇到某个协程阻塞会停止整个事件循环,从而阻止了其他协程继续执行,使用多线程防止阻塞
   loop.run_in_executor(ThreadPoolExecutor(), callback) 线程池+这个阻塞函数
   loop.call_soon_threadsafe(callback, *args) 将同步方法注册到新线程的loop去
   asyncio.run_coroutine_threadsafe(coroutine, loop)将异步方法注册到新线程的loop中去,返回值是concurrent.futures.Future对象,.result()获取返回结果
   3.9后使用 asyncio.to_thread(func, )

