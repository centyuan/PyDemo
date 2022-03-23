#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-31 下午3:36

"""
描述
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
语法
fromkeys()方法语法：
dict.fromkeys(seq[, value])
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
返回值
该方法返回一个新字典。
"""
#1:使用字典(dict 键不可变，不允许同一个键出现两次，后一个值会被记住)
# 且顺序保持不变
a=[1,2,4,2,4,5,6,5,7,8,9,0]
b={}
b=b.fromkeys(a) #默认值为None
c=list(b.keys())

#2.
a_list = [1,2,3,2,2,3,5,6,7,4,5,6,4,3,4]
new_list = []
for it in a_list:
    if it not in new_list:
        new_list.append(it)

#3.使用set 且保持顺序不变
test_list = ['cc', 'sss','ddd','bbbb', 'shafa','afa', 'sss', 'bbbb', 'cc', 'shafa']
list_1 = list(set(test_list))
list_1.sort(key=test_list.index)
print(list_1) #['cc', 'sss', 'ddd', 'bbbb', 'shafa', 'afa']

list_2 = sorted(set(test_list),key=test_list.index)
print(list_2)
['cc', 'sss', 'ddd', 'bbbb', 'shafa', 'afa']
#4.使用 set(集合是一个无序的不重复的元素序列) 但不保持顺序不变

print('set',list(set(a)))


a = ['a','c','d']
b = ['d','f','e']
m = zip(a,b)
print(type(m))
for i in m:
    print(i,type(i))
a1, a2 = zip(*zip(a,b)) #解压
