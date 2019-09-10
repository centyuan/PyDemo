#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-10 下午2:46

#方法一

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)

        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
            return cls.instance


class MyClass(object):
    __metaclass__ = Singleton


print(MyClass())
print(MyClass())

#方式二 使用装饰器

#。。。。


