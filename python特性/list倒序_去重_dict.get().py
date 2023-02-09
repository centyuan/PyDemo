# -*- coding:utf-8 -*-

# 一:list倒序
var = 'abcde'
print('var[2]:', var[2])
print('var', var[:-1])  # abcd
print('var', var[-2:])  # de
print('var', var[::-1])  # edcba 倒序
print('var', var[1::-1])  # ba 第0,1的倒序
print('var', var[::-1][-2:])  # ba 先倒序，在取后两位
print('var', var[::-1][:-2])  # edc
print('var', var[0:2][::-1])  # 先取正两位，在倒序

tmp = [1, 2, 3, 4, 5, 6]
print(tmp[5::-2])  # [6,4,2]

# 二:去重并保持顺序不变
# 1:使用字典(dict键不可变，不允许同一个键出现两次，后一个值会被记住) 且顺序保持不变
a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]
b = {}
# 窗口key为a的字典,value都为None
b.fromkeys(a)
c = list(b.keys())

# 2.not in
a_list = [1, 2, 3, 2, 2, 3, 5, 6, 7, 4, 5, 6, 4, 3, 4]
new_list = []
for it in a_list:
    if it not in new_list:
        new_list.append(it)

# 3.使用set 且保持顺序不变
test_list = ['cc', 'sss', 'ddd', 'bbbb', 'shafa', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
list_2 = sorted(set(test_list), key=test_list.index)
print(list_2)
['cc', 'sss', 'ddd', 'bbbb', 'shafa', 'afa']

# 4.使用 set(集合是一个无序的不重复的元素序列) 但不保持顺序不变

print('set', list(set(a)))
a = ['a', 'c', 'd']
b = ['d', 'f', 'e']
m = zip(a, b)
print(type(m))
for i in m:
    print(i, type(i))
a1, a2 = zip(*zip(a, b))  # 解压

# 三: 实现dict的get方法
l = ['a', 'b', 'c', 'd', 'e', 'f']
# enumerate()返回的是一个enumerate对象,利用它可以同时获得index和value
d = dict(enumerate(l))
print(d.get(3))
