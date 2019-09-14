#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午5:01

from types import FunctionType

#1内置函数 callable(func)

def functest():
    pass
print(callable(functest))

#2判断对象是否是FunctionType

if type(functest) is FunctionType:
    print(True)
if isinstance(functest,FunctionType):
    print(True)

#3判断对象是否实现__call__方法
if hasattr(functest,'__call__'):
    print('hasattr',True)