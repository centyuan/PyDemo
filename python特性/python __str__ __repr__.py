# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/21 15:32

class Me(object):
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
    def __str__(self):
        return ('__str__():'+self.name+self.hobby)
    def __repr__(self):
        return ('__repr__():'+self.name+self.hobby)

# 两个方法一定return
me = Me('freename', 'modify')
print(me)
print(str(me))
print(repr(me))