# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 21:55

"""
gevent:是一个基于协程的异步网络库，基于libev与greenlet(greenlet底层是C实现的) 遇到耗时的操作，自动切换协程
1.gevent对标准 I/O 函数做了猴子补丁。
gevent通过给标准库的socket、thread、ssl、os等打patch，采用隐式的方式，
无缝的把现有的各种库转换为支持异步，避免了为支持异步而重写，解决了库的问题,很大程度上解决大部分Python库不支持异步的问题
2.gevent提供了在libev和libuv（event loop）事件循环之上的一个high-level的同步API。


greenlet ：轻量级的并行编程，调度麻烦，用生成器实现的协程而且不是真正意义上的协程，只是实现代码执行过程中的挂起，唤醒操作。Greenlet 没有自己的调度过程，所以一般不会直接使用。
greenlet：http://greenlet.readthedocs.org/en/latest/

gevent：基于 libev 与 Greenlet 实现。不同于 Eventlet 的用 python 实现的 hub 调度，Gevent 通过 Cython 调用 libev 来实现一个高效的 event loop 调度循环。
同时类似于 Event，Gevent 也有自己的 monkey_patch，在打了补丁后，完全可以使用 python 线程的方式来无感知的使用协程，减少了开发成本。
gevent 官网文档：http://www.gevent.org/contents.html

"""
# 让异步操作返回future,future由gevent.spawn创建,使用一个函数和传递给这个函数的参数,并且启动了一个负责运行这个函数的greenlet
import time

from gevent import monkey, socket, pool
from gevent.lock import Semaphore
import gevent

# monkey.patch_all(thread=False)  # thread=False使多线程不阻塞
monkey.patch_all()  # 必须在前面打补丁


# 1.基本
def read(url):
    # print(gevent.getcurrent())  # 获取正在执行的greenlet
    print('open url:', url)
    gevent.sleep(2)
    return f'url:{url}'


start_time = time.time()
gevent.joinall([
    # spawn创建一个greenlet对象
    gevent.spawn(read, 'https://www.bilibili.com/'),
    gevent.spawn(read, 'https://www.mgtv.com/'),
    gevent.spawn(read, 'https://www.cctv.com/')
])
print('gevent执行time cost:', time.time() - start_time)

# 2.获取结果
# 一.g.value
greenlet_objs = [
    gevent.spawn(read, 'https://www.bilibili.com/'),
    gevent.spawn(read, 'https://www.mgtv.com/'),
    gevent.spawn(read, 'https://www.cctv.com/')
]
greenlet_objs_2 = gevent.joinall(greenlet_objs)
for index, g in enumerate(greenlet_objs):
    print('获取索引和结果', index, g.value)


# 二. iwait
def read(url):
    print('iwait open url', url)
    gevent.sleep(2)
    yield f'url:{url}'

def callback(obj):
    print('这是一个回调函数:',obj,obj.__dict__)


greenlet_objs = [
    gevent.spawn(read, 'https://www.bilibili.com/'),
    gevent.spawn(read, 'https://www.mgtv.com/'),
    gevent.spawn(read, 'https://www.cctv.com/')
]
greenlet_objs[0].link(callback)

for result in gevent.iwait(greenlet_objs):
    print('await生成器',result)
    for item in result.value:
        print('iwait 返回结果',item)

# 3.限制并发

# 一.Semaphore 信号量确保了同一时刻只有一定数量的协程能进入上下文模块
"""
from gevent.lock import Semaphore
semaphore = Semaphore(100)
# 1.使用上下文
with semaphore:
    yield requests.get(url).text
# 2.使用acquire和release
if semaphore.acquire():
    semaphore.release()

"""
# 二:Pool
"""
from gevent.pool import Pool
p = Pool(10)
tasks = []
for i in range(100):
    tasks.append(p.spawn(read,url))
gevent.joinall(tasks)

"""
# 4 常用方法说明
"""
gevent.spawn()                             创建一个普通的Greenlet对象并切换 
gevent.spawn_later(seconds=3)      延时创建一个普通的Greenlet对象并切换
gevent.spawn_raw()                      创建的协程对象属于一个组
gevent.getcurrent()                       返回当前正在执行的greenlet
gevent.joinall(jobs)                       启动事件循环执行协程，并等待结束，返回协程对象列表
gevent.wait()                                可以替代join函数等待循环结束，返回协程对象列表
gevent.kill()                                  杀死一个协程
gevent.killall()                               杀死一个协程列表里的所有协程
monkey.patch_all()                        非常重要，会自动将python的一些标准模块替换成gevent框架

 

> gevent常见用法

# Greenlet对象
from gevent import Greenlet

# Greenlet对象创建
job = Greenlet(target0, 3)
Greenlet.spawn()  # 创建一个协程并启动
Greenlet.spawn_later(seconds=3)  # 延时启动

# 协程启动
job.start()  # 将协程加入循环并启动协程
job.start_later(3)  # 延时启动

# 等待任务完成
job.join()  # 等待任务完成
job.get()  # 获取协程返回的值

# 任务中断和判断任务状态
job.dead()  # 判断协程是否死亡
job.kill()  # 杀死正在运行的协程并唤醒其他的协程，这个协程将不会再执行，可以
job.ready()  # 任务完成返回一个真值
job.successful()  # 任务成功完成返回真值，否则抛出错误

# 获取属性
job.loop  # 时间循环对象
job.value  # 获取返回的值

# 捕捉异常
job.exception  # 如果运行有错误，获取它
job.exc_info  # 错误的详细信息

# 设置回调函数
job.rawlink(back)  # 普通回调，将job对象作为回调函数的参数
job.unlink()  # 删除回调函数
# 执行成功的回调函数
job.link_value(back)
# 执行失败的回调函数
job.link_exception(back)

gevent.Pool的特殊方法：
pool.wait_available():等待直到有一个协程有结果
pool.dd(greenlet):向进程池添加一个方法并跟踪，非阻塞
pool.discard(greenlet):停止跟踪某个协程
pool.start(greenlet):加入并启动协程
pool.join():阻塞等待结束
pool.kill():杀死所有跟踪的协程
pool.killone(greenlet):杀死一个协程
 
"""