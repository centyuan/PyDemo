"""
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保创建的类在当前进程只有一个实例存在。

单例在单线程模型下，是线程安全的，不管怎么样创建实例，都有且只有一个，
面对多线程任务时，一般的单例代码无法承担多线程任务，当有io延时操作时，会生成id不同的实例，所以如果需要实现多线程单例，那么就在创建实例时增加线程锁;

https://www.cnblogs.com/huchong/p/8244279.html
https://cloud.tencent.com/developer/article/1673882
"""

# 方法一:使用模块 Python 的模块就是天然的单例模式
import threading

'''因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码'''


# 1.mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass


my_singleton = My_Singleton()


# 2.usaing:
# from mysingleton import my_singleon
# my_singleton.foo()

# 方式二:使用装饰器


def Singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(id(a1), id(a2))


# 三:__new__方法实现单例模式
class A:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj


# 四:加锁解决多线程问题

class Thread_A:
    # _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with Thread_A._instance_lock:
            if not hasattr(Thread_A, "_instance"):
                Thread_A._instance = super().__new__(cls)
            return Thread_A._instance
