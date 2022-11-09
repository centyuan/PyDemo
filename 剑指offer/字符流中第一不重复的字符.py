#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-22 下午12:05

"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""
from collections import Counter #计数器是对字典的补充，用于追踪对应值的出现次数 输出一个字典

class Solution:
    def __init__(self):
        self.words=[]

    def FirstAppearingOnce(self):
        remn=Counter(self.words)
        for char in self.words:
            if remn[char]==1:
                return  char
        return '#'

    def Insert(self,char):
        self.words.append(char)



# for char in ['a','b','d',3]:
#     print(char)