# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/22 2:46

"""
collections High-performance container datatypes
高性能容量数据类型。
"""
from collections import Counter
#counter 高性能计数器 对其中元素计数
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(c)
print(dict(c))

# 字符元素组成判定
if Counter('abcd3') == Counter('3acdb'):
    print(type(Counter('ab')))
    print("True")

ss = '[test33333]攻击静态DOMAIN-域名,并拿到了第一滴血'
print(ss.split('攻击了'))