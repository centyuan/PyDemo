#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-21 下午1:58
"""
问题:
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改

解决:
使用@property
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
(@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，
我们就拥有一个可控的属性操作：

getter
setter
"""
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value