# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 14:32

from collections import Counter

my_list = ['a', 'b', 'b', 'a', 'a', 'c', 'c', 'b', 'b']

# 1. 统计列表中元素出现的次数，返回一个列表元组
print(Counter(my_list))
# Counter({'b': 4, 'a': 3, 'c': 2})

# 2.出现次数最高的2个 Counter(my_list).most_common(2)
print(Counter(my_list).most_common(2))
# [('b', 4), ('a', 3)]
# 3.出现次数最多 Counter(my_list).most_
print(Counter(my_list).most_common()[0])  # 取出现次数最多的 a
result = dict(Counter(my_list))  # result返回字典
print(result)  # {'a': 3, 'b': 4, 'c': 2}
