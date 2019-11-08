# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/8 15:53

"""
Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。

所有的函数都是可调用对象。一个类实例也可以变成一个可调用对象，
只需要实现一个特殊方法__call__ ，我们把 Person 类变成一个可调用对象：
"""

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend, *args, **kwargs):
        print("my friend is:%s"%(friend))

p = Person('Bob', 'male')
p("cob")


