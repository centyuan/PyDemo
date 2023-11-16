"""
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保创建的类在当前进程只有一个实例存在。

单例在单线程模型下，是线程安全的，不管怎么样创建实例，都有且只有一个，
面对多线程任务时，一般的单例代码无法承担多线程任务，当有io延时操作时，会生成id不同的实例，所以如果需要实现多线程单例，那么就在创建实例时增加线程锁;

https://www.cnblogs.com/huchong/p/8244279.html
https://cloud.tencent.com/developer/article/1673882
"""

# 方法一:使用import Python 的模块就是天然的单例模式
import threading
from typing import Any

'''因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码'''


# 1.mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass


my_singleton = My_Singleton()

# 2.usaing:
# from mysingleton import my_singleon
# my_singleton.foo()

# 方式二:使用装饰器(函数装饰器和类装饰器都可以)

def Singleton(cls):
    _instance = {}
    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper

class Snigleton(object):
    def __init__(self, cls) -> None:
        self._cls = cls
        self._instance = {}
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]
@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
print("2装饰器:",a1,id(a1))
print("2装饰器:",a2,id(a2))


# 三:__new__方法实现单例模式
class Singletion(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# 四:加锁解决多线程问题

class Thread_A:
    # _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with Thread_A._instance_lock:
            if not hasattr(Thread_A, "_instance"):
                Thread_A._instance = super().__new__(cls)
            return Thread_A._instance

# 五:使用元类metaclass方式实现

class SingletonType(type):
    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        obj = cls.__new__(cls, *args, **kwds)
        cls.__init__(obj, *args, **kwds)
        return obj
    