"""
1.找最小或最大值
2.将最下或最大值加入新数组
3.再从剩余找最小或最大

时间复杂度:O(n平方),不稳定
"""


def find_samllest(arr):
    small_ = arr[0]
    small_index = 0

    for i in range(1,len(arr)):
        if arr[i] < small_:
            small_ = arr[i]
            small_index = i
    return small_,small_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        small_,small_index = find_samllest(arr)
        new_arr.append(arr.pop(small_index))
    return new_arr
