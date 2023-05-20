###引言
>asyncio作为python协程的标准实现,使用事件循环驱动的协程实现并发,已在python3.4纳入标准库,本文是在使用asyncio过程中,抛出的几个疑问及相关思考和整理
>概述:子程序或函数在程序执行过程中,通过栈实现的层级调用。而协程在内部执行时可以中断去执行别的子程序,可以简单理解协程作为轻量级的线程。

**1.基本描述**
    1.event_loop事件循环:协程函数注册到事件循环上,会依次相应的执行,支持注册Future和task类型的对象
    2.coroutine协程对象:async定义的函数,返回一个协程对象，函数的最终执行交给event_loop
    3.future:是对协程的封装(提供了取消/回调等),代表一个未来对象,执行结束后会把最终结果设置到Future对象上,属于底层对象,日常开发使用task
    4.task任务:是future的子类,对future再一次的封装

**2.协程实现的几种方式?**
    - python2.X:利用生成器通过yield+send实现协程
    - python3.4:利用asyncio+yield from实现协程
    - python3.5:asyncio+async/await(比较熟悉)
      - python3.7:引入了asyncio.create_task和asyncio.run两个高级接口
  

**3.正确姿势**
```
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
    retunr "do3"

async def main():
    # 方式1.wait/gather实现并发
    #done,pending = await asyncio.wait(do1(),do3()) 
    return_1,return_3 = await asyncio.gather(do1(),do3())

def perf_(func)：
    start = time.perf_counter()
    asyncio.run(func())
    print(f"{func.__name"花费：{time.perf_count()-start}})

if __name__ =="__main__":
    perf_(main())
```

