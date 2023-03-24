"""
遍历一个集合中元素的所有可能的排列或组合
"""
# 1.排列
from itertools import permutations
items = ['a','b','c']
for p in permutations(items):
    print(p)

"""
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')

"""
# 2.可选长度的排列
for p in permutations(items,2):
    print(p)
"""
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
"""
from collections import defaultdict
