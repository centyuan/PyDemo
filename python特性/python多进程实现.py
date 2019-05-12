#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午8:31

from multiprocessing import Process,Pool #多进程

def f(name):
    print('hello',name)
def fpool(x):
    return x*x

if __name__ =='__main___':
    p=Process(target=f,args=('centyuan',))
    p.start()
    p.join()
    #进场池
    with Pool(5) as p:
        print(p.map(fpool,[1,2,3]))



