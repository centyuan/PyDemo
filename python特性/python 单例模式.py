#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-10 下午2:46
"""
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保创建的类在当前进程只有一个实例存在。
当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

"""
#方法一 使用模块 Python 的模块就是天然的单例模式
'''因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码'''

#https://www.cnblogs.com/shenbuer/p/7724091.html
#方式二 使用装饰器
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
a1 = A(2)
a2 = A(3)
print(id(a1),id(a2))




