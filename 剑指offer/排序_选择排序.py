"""
1.找最小或最大值
2.将最小或最大值加入新数组
3.再从剩余找最小或最大

时间复杂度:O(n平方),不稳定
无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，
数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。
"""

def selection_sort(arr):
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex = j
        # 如果i不是最小的,就交换
        if minindex !=i:
            arr[i],arr[minindex] = arr[i],arr[minindex]
    return arr