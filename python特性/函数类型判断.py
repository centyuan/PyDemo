#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-5 下午8:07

import  types

def func(arg):
    #if callable(arg):
    if isinstance(arg,types.FunctionType):
        print(arg())
    else:
        print(arg)


func(123)
func(lambda :'666')
