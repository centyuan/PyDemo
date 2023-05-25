###引言

> asyncio作为python协程的标准实现,使用事件循环驱动的协程实现并发,已在python3.4纳入标准库,本文是在使用asyncio过程中,基本使用和整理
> 概述:子程序或函数在程序执行过程中,通过栈实现的层级调用。而协程在内部执行时可以中断去执行别的子程序,可以简单理解协程作为轻量级的线程。

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

**3.正确使用姿势**

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
    # 方式1:通过wait/gather实现并发
    # done,pending = await asyncio.wait(do1(),do3()) 
    return_1,return_3 = await asyncio.gather(do1(),do3())
 
    # 方式2:通过ensure_future或create_task创建任务,在await实现并发
    task1 = asyncio.ensure_future(do1())
    task3 = asyncio.ensure_future(do3())
    await task1
    await task3

    # 方式3:直接await不能实现并发
    await do1()
    await do3()


def perf_(func)：
    start = time.perf_counter()
    asyncio.run(func())
    print(f"{func.__name"花费：{time.perf_count()-start}})

if __name__ =="__main__":
    perf_(main())

```

**4.两种方案获取返回值**

> 1.通过回调add_done_callback()
> 2.通过task.result()接口,若任务没有完成,result()不会阻塞去等待结果,而是直接抛出asyncio.InvalidStateError异常

**one:回调**

```

import asyncio

def callback(future):
    print("返回值:",future.result())

async def return_data():
    await asyncio.sleep(1)
    return "to be or not to be"

if __name__ =="__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(return_data())
    task.add_done_callback(callback)
    loop.run_until_complete(task)
    loop.close()
```

**two:task**

```
import asyncio
import time


now = lambda:time.perf_counter()

async def do_something(t:int):
    print("嵌套waiting:",t)
    await asyncio.sleep(t)
    return f"嵌套Cose {t}s"


# 1.main处理结果
async def main1():
    coroutines = [do_something(2) for t in range(1,100)]
    tasks = [asyncio.ensure_future(coroutine) for coroutine in coroutines]
    done,pending = await asyncio.wait(tasks)
    for task in done:
        print("返回结果1:",task.result())
  
# 2.await返回
async def main2():
    coroutines = [do_something(2) for t in range(1,100)]
    tasks = [asyncio.ensure_future(coroutine) for coroutine in coroutines]
    return await asyncio.wait(tasks)
  
# 3.gather
async def main3():
    coroutines = [do_something(2) for t in range(1,100)]
    tasks = [asyncio.ensure_future(coroutine) for coroutine in coroutines]
    return await asyncio.gather(*tasks)

def show_perf(func):
    start_= now()
    loop = asyncio.get_event_loop()
    # 1.
    # loop.run_until_complete(func())
    # 2.
    # done,pending = loop.run_until_complete(func())
    # for task in done:
    #     print("返回结果2:",task.result())
    # 3.
    results = loop.run_until_complete(func())
    for result in results:
        print("返回结果3:",result)

    print("perf:",now()-start_)
  

if __name__=="__main__":
    # show_perf(main1)
    # show_perf(main2)
    show_perf(main3)

```

**5.不要使用asyncio.create_task创建后台任务**
[create_task存在的问题](https://www.bilibili.com/read/cv17261955)
[cpython-issue](https://github.com/python/cpython/issues/91887)
asyncio仅仅会保留对Task的弱引用weakref,而弱引用不会阻止对象被python垃圾回收机制回收,可能导致正在运行的task被回掉

```
# asyncio.create_task(back_task())
# task was destroyed but it is pending
# 解决方案是对创建的task强引用
task = asyncio.create_task(back_task())
```

**6.其他说明**

```
1. wait和gather的区别
wait:默认情况下,会等待全部任务完成,所以pending默认是空的,可以使用return_when参数来决定返回时机
return_when:ALL_COMPLETED(默认全部返回),FIRST_COMPLETED(完成一个返回),FIRST_EXCEPTION(异常一个返回)
done, pending = await asyncio.wait(tasks:list[task])  # 传入task列表，done为已完成的task列表
gather:返回task执行的结果
results = await asyncio.gather(*tasks)    # 传入多个task,可以使用*tasks

1. get_event_loop和new_event_loop,set_event_loop区别
主线程:get_event_loop会创建一个event_loop，并且多次调用始终返回该loop
其他线程:get_event_loop会报错,正确的使用是 loop=asyncio.new_event_loop asyncio.set_event_loop(loop)


3. asyncio.create_task vs asyncio.ensure_task vs loop.create_task
(1.都是创建task的方法,asyncio.create_task为3.7新增的高阶用法
(2.asyncio.create_task就是使用的loop.create_task
(3.loop.create_task的参数是coroutine
(4.asyncio.ensure_task可以是(coroutine/Future/awaitable对象[实现__await__方法])
    -coroutine对象:还是使用loop.creat_task
    -Future对象:直接返回
    -awaitable对象:会await这个对象的__await__方法,在执行一次ensure_task,最后返回task/future
4. asyncio.run
asyncio.run():为3.7新增的高级接口,隐式的创建loop去执行task,直接asyncio.run(main())
asyncio.create_task:为3.7新增的高级接口,创建任务

```
