# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 20:46
"""
查找集:必须有序
时间复杂度:
最多:O(log N)
最少:O(1)

特别是当列表本身就已经排过序的情况下，用二分搜索进行对象查找（复杂度
O(log n)）比将列表转换成字典然后进行查询要更高效（虽然字典查找复杂度
是 0(1)，字典转换复杂度却是 O(n)。而且字典要求没有重复的键，你可能不希
望受到这样的限制）
"""


def bin_search(data_set, value, low, high):
    if low <= high:
        # 向下取整
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            bin_search(data_set, value, low, mid - 1)
        elif data_set[mid] < value:
            bin_search(data_set, value, mid + 1, high)
    else:
        return


def bin_search(data_list, value):
    low = 0
    high = len(data_list)
    while low <= high:
        mid = (low + high) // 2
        if value == data_list[mid]:
            return mid
        elif value > data_list[mid]:
            low = mid + 1
        elif value < data_list[mid]:
            high = mid - 1

# python bisect(二分查找轮子)
import bisect
L = [1,3,3,4,6,8,12,15]
x_sect_point = bisect.bisect_left(L, 3)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置
print(x_sect_point)  # 1
x_sect_point = bisect.bisect_left(L, 5)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置
print(x_sect_point)  # 4

x_sect_point = bisect.bisect_right(L, 3)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置
print(x_sect_point)  # 3
x_sect_point = bisect.bisect_right(L, 5)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置
print(x_sect_point)  # 4

bisect.insort_left(L, 2)  # 将x插入到列表L中，x存在时插入在左侧
print(L)  # [1, 2, 3, 3, 4, 6, 8, 12, 15]

bisect.insort_right(L, 4)  # 将x插入到列表L中，x存在时插入在右侧
print(L)  # [1, 2, 3, 3, 4, 4, 6, 8, 12, 15]