"""
协程间的通信:基本使用共享内存的方式
"""
# 1.共享变量
"""
共享变量可以说全局变量，或类属性,如何同步机制(如锁)来保证数据的一致性

import asyncio

count = 0
async def producer():
    global count
    while True:
        count +=1
        print(f"Producer:{count}")
        await asyncio.sleep(1)
    
async def consumer():
    global count
    while True:
        if count > 0:
            count -=1
            pritn(f"Consumer:{count}")
        await asyncio.sleep(2)

async def main():
    await asyncio.gather(producer(), consumer())

if __name__ == "__main__":
    asyncio.run(main())
"""

# 2.Queue 常见的通信方式，它是一个先进先出FIFO数据结构
# syncio.Queue()是个异步队列
"""
import asyncio 

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        queue.put(i)
        print(f"Producer:{i}")

async def consumer(queue):
    while True:
        data = queue.get()
        print(f"Consumer:{data}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(producer_task,consumer_task)
    await queue.join()   # 等待队列中所有数据被处理完
"""

# 3.Future
"""
import asyncio

async def coroutine(future):
    await asyncio.sleep(1)
    future.set_result("Data from coroutine")

async def main():
    future = asyncio.Future()
    asyncio.create_task(coroutine(future))
    result = await future
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())

"""
