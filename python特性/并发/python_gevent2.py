# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/10 21:55

"""
遇到IO阻塞,自动切换任务
"""
from gevent import monkey
import gevent
import time
from urllib.request import urlopen
monkey.patch_all()

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