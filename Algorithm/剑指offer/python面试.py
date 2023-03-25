# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-9 下午5:23

# 1.类继承
class A:
    def show(self):
        print('base show ')


class B(A):
    def show(self):
        print('derived show')


obj = B()
obj.show()
# 如何调用类A的show方法，
obj.__class__ = A  # __class__ 方法指向了类对象，用完记得修改回来
obj.show()


# 2.方法对象
class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num, *args, **kwargs):
        print('call:', num + self.__a)


a1 = A(10, 20)
a1.myprint()
a1(90)  # 为了对象实例能被直接调用，需要实现__call__方法


# 3.new和init
class B:
    def fn(self):
        print('B fn')

    def __init__(self):
        print('B INIT')


class A(object):
    def fn(self):
        print('A fn')

    # 使用__new__方法，可以决定返回那个对象，这个可以用于设计模式的单例，工厂模式。
    def __new__(cls, a, *args, **kwargs):
        print('NEW', a)
        if a > 10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self, a):
        print('INIT', a)


a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()


# 4.默认方法
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self):
        print('default')

    def __getattr__(self, item):  # 只有当没有定义的方法调用时，才会调用它
        return self.mydefault()


a1 = A(10, 20)
a1.fn1()  # fn1方法没有定义时，会调用默认方法

# 5.包管理
"""
一个包里有mod1.py,mod2.py,mod3.py,
使用from demopack import *导入模块时
在 __init__.py中增加 __all__ = ['mod1','mod2']#就只会导入mod1,mod2
"""


# 6.闭包
def mulby(num):
    def gn(val):
        return num * val

    return gn


fu = mulby(7)
print(fu(9))
