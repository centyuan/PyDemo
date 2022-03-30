# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 20:46

def bin_search(data_set,value,low,high):
    if low <=high:
        mid = (low+high)//2
        if data_set[mid]==value:
            return mid
        elif data_set[mid]>value:
            bin_search(data_set,value,low,mid-1)
        else:
            bin_search(data_set,value,mid+1,high)

    else:
        return


def bin_search(data_set,value,low,high):
    if low<=high:
        mid = (low+high)//2
        if data_set[mid]==value:
            return mid
        elif data_set[mid] > value:
            bin_search(data_set,value,low,mid-1)
        elif data_set[mid] < value:
            bin_search(data_set,value,mid+1,high)
