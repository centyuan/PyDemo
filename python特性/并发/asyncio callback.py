import asyncio
"""
有2种方案可以获取返回值
1:可通过调用 task.result() 方法来获取协程的返回值，
但是只有运行完毕后才能获取，若没有运行完毕，result()方法不会阻塞去等待结果，
而是抛出 asyncio.InvalidStateError 错误

2:通过add_done_callback()回调
https://zhuanlan.zhihu.com/p/59621713
"""
def time__():
    for i in range(50):
        print("---:", i)
    return "time"

async def do_some_work(i):
    print('start:', i)
    await asyncio.sleep(i)
    time__()
    print('end:', i)
    return "++++:"+str(i)

def callback1(future):
    print("回调函数-返回结果:",future.result())
def callback2(future):

    print("回调函数-返回结果:", future.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coroutine_1 = do_some_work(2)
    coroutine_2 = do_some_work(3)
    # loop.create_task(coroutine) 接收一个协程，返回asyncio.Task,也是asyncio.Future(task是Future子类)
    task1 = loop.create_task(coroutine_1) # 通过loop.create_task(croutine_1)创建任务
    task1.add_done_callback(callback1)  # 任务绑定回调函数
    task2 = loop.create_task(coroutine_2)
    task2.add_done_callback(callback2)
    # 通过asyncio.wait()可以控制多任务
    # 传入的参数是future或协程构成的可迭代对象。最后将返回值传给run_until_complete()加入事件循环
    loop.run_until_complete(asyncio.wait([task1,task2]))
    # loop.run_until_complete(asyncio.gather(*[task1,task2])) # asyncio.gather high-level
    # task.result() 方法来获取协程的返回值
    print(task1.result(),task2.result())
