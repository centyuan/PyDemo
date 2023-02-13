# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/22 2:46

"""
collections High-performance container datatypes
高性能容量数据类型。
"""
from collections import Counter

# 1.counter 高性能计数器 对其中元素计数
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(c)
# Counter({'blue': 3, 'red': 2, 'green': 1})
print(dict(c))
# {'red': 2, 'blue': 3, 'green': 1}

# 2.字符元素组成判定
if Counter('abcd3') == Counter('3acdb'):
    print(type(Counter('ab')))
    print("True")


