#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-31 下午3:36

"""
描述
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

语法
fromkeys()方法语法：

dict.fromkeys(seq[, value])
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
返回值
该方法返回一个新字典。
"""
a=[1,2,4,2,4,5,6,5,7,8,9,0]
b={}
b=b.fromkeys(a)
c=list(b.keys())