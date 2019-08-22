#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午9:46

"""
在python3中的zip函数,可以把两个或两个以上的迭代器封装为生成器
"""
names = ['Cecilia','Lise','Marie']
letters = [len(n) for n in names]
