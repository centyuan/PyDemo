# -*- coding:utf-8 -*-
# Author centyuan


"""
__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员
"""


class Me(object):
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def __str__(self):
        return ('__str__():' + self.name + self.hobby)

    def __repr__(self):
        return ('__repr__():' + self.name + self.hobby)


# 两个方法一定return
me = Me('freename', 'modify')
print('me:', me)
print('str:', str(me))
print('repr:', repr(me))
