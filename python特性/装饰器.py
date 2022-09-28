# -*- coding:utf-8 -*-
import time

"""
＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西（取决于装饰器的返回值），
1如果装饰器函数的返回值为普通变量，那么被修饰的函数名就变成了变量名；
2如果装饰器返回的是一个函数的名称，那么被修饰的函数名依然表示一个函数
"""

"""1:带参数的装饰器 嵌套一个函数，该函数带有的参数个数和被装饰器修饰的函数相同"""


def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("2:带参数的装饰器 say:", arc)
        fn(arc + "AAAAAAAAAA")

    return say


@funA
def funB(arc):
    print("2:带参数的装饰器 funB:", arc)


# 等价于
# funB = funA(funB)
# funB("str")
funB("http://c.biancheng.net/python")

"""2:多个参数 ，*args 和 **kwargs 表示接受任意数量和类型的参数。"""


def funA(fn):
    # 定义一个嵌套函数
    def say(*args, **kwargs):
        print('funA 中say')
        fn(*args, **kwargs)

    return say


@funA
def funB(arc):
    print("funB:C语言中文网：", arc)


@funA
def funC(name, arc):
    print(name, arc)


funB("http://c.biancheng.net")
funC("other_funB:Python教程：", "http://c.biancheng.net/python")

"""
使用装饰器时，有一些细节需要注意：被装饰后的函数其实已经是另一个函数了，它的函数名及属性等，都是属于新函数，
所以,Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用
例如打印:
被装饰函数的.__doc__
被装饰函数的.__name__
"""
"""3:多个装饰器"""
from functools import wraps


def deco01(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("装饰器1")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("时间为%d ms" % msecs)
        print("装饰器1结束")

    return wrapper


def deco02(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("装饰器2")
        print("装饰器2结束")

    return wrapper


@deco01
@deco02
def func(a, b):
    print("func开始")
    time.sleep(1)
    print("func结束 %d" % (a + b))


func(3, 4)
