# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:20

a = ['a', 'b', 'c', 'd']
b = ['a', 'b', 'e', 'f']
set_a = set(a)
set_b = set(b)
# 1. a中有，b中没有的
comparsion = set_a - set_b
print(comparsion)
# 2. b中有,a中沒有的
comparsion = set_b - set_a
print(comparsion)
# 3. a中有，b中没有的:set_a.difference(set_b)
comparsion = set_a.difference(set_b)
print(comparsion)
