"""
函数装饰器:
 1.装饰器是可调用函数,参数是一个函数,返回另一个函数或可调用对象，用于在源码中标记函数,已某种方式增强函数的行为
 2.装饰器在加载模块时立即执行

使用装饰器时，有一些细节需要注意：被装饰后的函数其实已经是另一个函数了，原有的的函数名等属性都会丢失。
例如打印:
被装饰函数的.__doc__
被装饰函数的.__name__
解决办法:
 1. from functools import update_wrapper
   return update_wrapper(wrapper, func) 
 2. from functools import wraps  # 是对update_wrapper更高级的封装
  @wraps
    保证被装饰函数还拥有原有属性,消除使用了装饰器的函数结构改变(如不支持关键字参数且覆盖了__name,__doc__属性)

"""


import time
from functools import wraps
from functools import update_wrapper

# 1.函数装饰器

def time_calc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        speed_time = time.perf_counter()-start_time
        return result
    return wrapper

# 2.带参数的装饰器(采用三层函数定义装饰器)

def valid_permission(per):
    def valid_(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("2:装饰器接受参数",per)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return valid_

@valid_permission(per="可执行")
def hello(a,b):
    print("2:",a,b)

hello(1,2)


# 3.多个装饰器


def deco01(func):
    @wraps(func)  # 1.保证原有属性
    def wrapper(*args, **kwargs):
        print("3:装饰器1开始")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("3:装饰器1时间为%d ms" % msecs)
        print("3:装饰器1结束")

    return wrapper   # 2保证原有属性.return update_wrapper(wrapper, func) 


def deco02(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("3:装饰器2开始")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("3:装饰器2时间为%d ms" % msecs)
        print("3:装饰器2结束")

    return wrapper


@deco01
@deco02
def func(a, b):
    print("3:func开始")
    time.sleep(1)
    print("3:func结束 %d" % (a + b))


func(3, 4)

# 4.类装饰器(类作为装饰器,实质使用了类方法的__call__来实现类的直接调用,类中定义__call__,类作为装饰器,会运行__call__内容)
    
class Animal:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("4:类装饰器Animial的__call__")
        return self.func(*args, **kwargs)


@Animal
def test(name, kind):
    print("4:test running")
    return f"{name}属于{kind}"

test("name","kind")

# 5.为类加装饰器(可以修改类属性,类方法)


def decorator(func):
    def wrapper(cls):
        # 为类添加属性
        cls.name = "张三"
        # 为类添加方法
        cls.work = func
        return cls
    return wrapper

def printd(*args):
    print("5:类中printd函数")


@decorator(printd)
class Dog:
    def __init__(self):
        printd("5:类Animal的init方法")


dog = Dog()
dog.do_some()
print()