#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-28 下午4:05
"""
sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键，
所以那些试图从代码来说明它作用的解释一直没看明白。因为我们从外部取得的参数可以是多个，
所以获得的是一个列表（list)，也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。
其第一个元素是程序本身，随后才依次是外部给予的参数。
"""
import  sys
a=sys.argv[0]
print(a)
print(sys.argv[2],sys.argv[1])
