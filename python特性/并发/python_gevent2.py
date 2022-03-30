# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 21:55

"""
Gevent实现遇见IO自动切换的功能，
需要调用如下代码from gevent import monkey; monkey.patch_all()实现，且处于该代码下面的代码才能自动切换，处于代码前面的代码不能自动切换
"""

import gevent
import time
from urllib.request import urlopen
#thread=False使多线程不阻塞
from gevent import monkey;monkey.patch_all(thread=False)

def read(url):
    print("open url:",url)
    resu = urlopen(url)
    if resu:
        data = resu.read()
        print(len(data),url)
start_time = time.time()
read("https://www.bilibili.com/")
read("https://www.mgtv.com/")
print("普通--time cost",time.time()-start_time)
start_time = time.time()
gevent.joinall([
    gevent.spawn(read,'https://www.bilibili.com/'),
    gevent.spawn(read,'https://www.mgtv.com/')
])
print("gevent--time cost",time.time()-start_time)