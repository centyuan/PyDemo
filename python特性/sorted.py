# -*- coding:utf-8 -*-
"""
sorted() 函数对所有可迭代的对象进行排序操作。
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

"""
from functools import cmp_to_key

l = [('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
sorted(l, key=lambda x: x[0])
print(sorted(l, key=lambda x: x[0]))
# [('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]

sorted(l, key=lambda x: x[0], reverse=True)
print(sorted(l, key=lambda x: x[0], reverse=True))
# [('e', 3), ('d', 4), ('c', 6), ('b', 2), ('a', 1)]

sorted(l, key=lambda x: x[1])
print(sorted(l, key=lambda x: x[1]))
# [('a', 1), ('b', 2), ('e', 3), ('d', 4), ('c', 6)]

sorted(l, key=lambda x: x[1], reverse=True)
print(sorted(l, key=lambda x: x[1], reverse=True))
# [('c', 6), ('d', 4), ('e', 3), ('b', 2), ('a', 1)]
# x就代表列表里的每一个元素

print(sorted(l, key=lambda x: (x[1], x[0])))
# 如果我们想用第二个关键字
# 排过序后再用第一个关键字进行排序呢
# sorted(iterable[, cmp[, key[, reverse]]])
# 参数说明：

# iterable -- 可迭代对象。
# cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

Firewall_data = [
    {"name": 'Y', "type": 'FireWall', "create_time": "2022-09-10"},
    {"name": 'B', "type": 'FireWall', "create_time": "2022-09-11"},
    {"name": 'A', "type": 'FireWall', "create_time": "2022-09-12"},
    {"name": 'D', "type": 'FireWall', "create_time": "2022-09-13"},
]

print(sorted(Firewall_data, key=lambda x: x.get('create_time'), reverse=True))


#   python3 sorted() 去掉cmp参数, 使用cmp_to_key 转换函数
#   排序规则函数(先比较score，在比较time)
def fun_sorted(x, y):
    if x['socre'] > y['score']:
        return 1
    if x['score'] < y['score']:
        return -1
    if x['score'] == y['score']:
        if x['time'] > y['time']:
            return -1
        else:
            return 1


rank = [{"score": i, "time": '726' + str(i)} for i in range(10)]
new_rank = sorted(rank, cmp_to_key(fun_sorted), reverse=True)
