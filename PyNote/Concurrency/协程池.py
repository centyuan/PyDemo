
import asyncio
import queue
import time
from threading import Thread

import aiohttp


class AsyncPool:
    """
    1.动态添加任务
    2.支持自动停止事件循环
    3.支持最大协程数
    """
    def __init__(self,maxsize=1,loop=None):
        self.task = queue.Queue()
        self.loop,_ = self.start_loop(loop)
        self.semaphore = asyncio.Semaphore(maxsize, loop=self.loop)

    
    def task_add(self, item=1):
        """添加任务"""
        self.task.put(item)

    def task_done(self,fn):
        """任务完成"""
        if fn:
            pass
        self.task.get()
        self.task.task_done()
    
    @property
    def running(self):
        """获取当前任务数"""
        return self.task.qsize()

    @staticmethod
    def _start_thread_loop(loop):
        asyncio.set_event_loop(loop) # 设置为当前上下文的事件循环
        loop.run_forever()   # 开始事件循环

    async def _stop_thread_loop(self, loop_time=1):
        """停止协程"""
        while True:
            if self.task.empty():
                self.loop.stop()  #停止协程
                break
            await asyncio.sleep(loop_time)
        
    def start_loop(self,loop):
        """开启新线程运行事件循环"""
        if not loop:
            loop = asyncio.new_event_loop()
        loop_thread = Thread(target=self._start_thread_loop,args=(loop,))
        loop_thread.setDaemon(True)  # 设置为守护线程
        loop_thread.start()    # 运行线程同时协程事件循环也会执行
        return loop,loop_thread

    def stop_loop(self,loop_time=1):
        """队列为空,则关闭线程"""
        asyncio.run_coroutine_threadsafe(self._stop_thread_loop(loop_time), self.loop)

    def release(self, loop_time=1):
        """释放线程"""
        self.stop_loop(loop_time)

    async def async_semaphore_func(self, func):
        """信号包装"""
        async with self.semaphore:
            return await func

    def submit(self,func,callback=None):
        """提交任务到事件循环"""
        self.task_add()
        # 将协程注册到一个运行在线程中的循环,
        future = asyncio.run_coroutine_threadsafe(self.async_semaphore_func(func), self.loop)
        # 添加回调函数,添加顺序调用
        future.add_done_callback(callback)
        future.add_done_callback(self.task_done)

async def thread_example(i):
    url = "http://127.0.0.1:8080/app04/async4?num={}".format(i)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            # print(res.status)
            # print(res.content)
            return await res.text()


def my_callback(future):
    result = future.result()
    print('返回值: ', result)




def main():
    # 任务组， 最大协程数
    pool = AsyncPool(maxsize=100000)

    # 插入任务任务
    for i in range(100000):
        pool.submit(thread_example(i), my_callback)

    print("等待子线程结束1...")
    # 停止事件循环
    pool.release()

    # 获取线程数
    # print(pool.running)
    print("等待子线程结束2...")
    # 等待
    pool.wait()

    print("等待子线程结束3...")
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("run time: ", end_time - start_time)


aiopools 