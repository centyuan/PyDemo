# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/22 2:57

from collections import Counter
#counter 高性能计数器 对其中元素计数
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (dict(c))
# 字符元素组成判定
from collections import Counter
if Counter('abcd3') == Counter('3acdb'):
    print(type(Counter('ab')))
    print("True")