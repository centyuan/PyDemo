# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/22 3:06
#给定具体的大小，定义一个函数以按照这个大小切割列表。

from math import ceil
# ceil返回数字的上入整数
def chunk(lst, size):
    return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(0, ceil(len(lst) / size))))
    )
result = chunk([1,2,3,4,5],2)
print(result)
# [[1,2],[3,4],5]
