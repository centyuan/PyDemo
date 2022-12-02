# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 20:46
"""
查找集:必须有序
二分查找最多需要:log 2 N 次
时间复杂度:O(log 2 N)
"""


def bin_search(data_set,value,low,high):
    if low <=high:
        # 向下取整
        mid = (low+high)//2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            bin_search(data_set,value,low,mid-1)
        elif data_set[mid] < value:
            bin_search(data_set,value,mid+1,high)
    else:
        return

def bin_search(data_list,value):
    low = 0
    high = len(data_list)-1
    while low <=high:
        mid = low+high//2
        if data_list[mid] == value:
            return mid
        if data_list[mid] > value:
            high = mid-1
        else:
            low = mid +1
