# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 21:55

"""
gevent 对标准 I/O 函数做了猴子补丁，把它们变成了异步
from gevent import monkey; monkey.patch_all()实现，
处于该代码下面的代码才能自动切换，处于代码前面的代码不能自动切换
gevent是coroutine(大部分翻译为: 协程)，基于Python的greenlet。
gevent提供了在libev和libuv（event loop）事件循环之上的一个high-level的同步API。

"""
import asyncio
import gevent
import time
import requests
from gevent import monkey

monkey.patch_all(thread=False)  # thread=False使多线程不阻塞


def read(url):
    print("open url:", url)
    time.sleep(4)
    print('time后')
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    # }
    # resu = requests.get(url,headers=headers,verify=False)
    # if resu:
    #     data = resu.read()
    #     print(len(data),url)


# 1.普通顺序执行
start_time = time.time()
read("https://www.bilibili.com/")
read("https://www.mgtv.com/")
print("普通--发费time cost:", time.time() - start_time)

# 2.使用gevent
start_time = time.time()
gevent.joinall([
    gevent.spawn(read, 'https://www.bilibili.com/'),
    gevent.spawn(read, 'https://www.mgtv.com/')
])
print("gevent--发费time cost:", time.time() - start_time)


async def comsumer():
    print('consumer_start 1:', time.time())
    await asyncio.sleep(4)
    print('consumer_end 2"', time.time())


start_time = time.time()
loop = asyncio.get_event_loop()
tasks = [comsumer() for i in range(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print('asyncio--发费time cost:', time.time() - start_time)

