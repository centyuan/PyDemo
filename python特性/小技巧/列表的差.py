# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:20

a = ['a','b','c','d']
b = ['a','b','e','f']
set_a = set(a)
set_b = set(b)
comparsion = set_a.difference(set_b) #a中有，b中没有的
print(list(comparsion))

