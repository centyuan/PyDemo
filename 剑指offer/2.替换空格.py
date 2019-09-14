#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午9:31

"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution:
    def replaceSpace(self,s):
        return  "%20".join(s.split(" "))