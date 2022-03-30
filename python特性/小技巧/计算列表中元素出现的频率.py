# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 14:32

from collections import  Counter

my_list = ['a','b','b','a','a','c','c','b','b']

#统计列表中元素出现的次数，返回一个列表元组
print(Counter(my_list)) #Counter({'b': 4, 'a': 3, 'c': 2})
print(Counter(my_list).most_common())#[('b', 4), ('a', 3), ('c', 2)]
print(Counter(my_list).most_common()[0]) #取出现次数最多的 a

