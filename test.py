import asyncio


class CoroutinePool:
    def __init__(self, max_works):
        self.max_works = max_works
        self.tasks = []
        self.task_queue = asyncio.Queue()

    def submit_task(self, task, *args, **kwargs):
        self.task_queue.put_nowait([task, args, kwargs])

    async def __aenter__(self):
        for i in range(self.max_works):
            # asyncio.create_task(self._task_handle())
            self.tasks.append(asyncio.create_task(self._task_handle()))

        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.task_queue.join()

        for task in self.tasks:
            task.cancel()

        await asyncio.gather(*self.tasks, return_exceptions=True)

    async def _task_handle(self):
        while True:
            task, args, kwargs = await self.task_queue.get()
            await task(*args, **kwargs)
            self.task_queue.task_done()




async def f(i):
    await asyncio.sleep(1)
    print(i, asyncio.current_task().get_name())


async def main():
    async with CoroutinePool(5) as pool:
        for i in range(10):
            pool.submit_task(f, i)
    if pool.task_queue.empty():
        print("pool.task_queue.empty()",pool.task_queue.empty())
    else:
        print("pool.task_queue.empty()",pool.task_queue.empty())
    get_nowait = pool.task_queue.get_nowait()
    print("get_nowait",get_nowait)

if __name__ == "__main__":
    asyncio.run(main())

