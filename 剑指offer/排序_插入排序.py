"""
1.对于未排序数据，在已排序序列中从后向前扫描，
2.找到相应位置并插入。

时间复杂度:最好-O(n)最坏-O(n平方)
"""

def insert_sort(arr):
    for i in range(len(arr)):
        preindex = i-1
        current = arr[i]
        while preindex >=0 and current < arr[preindex]:
            # 比前一个值小,前一个往后移一位
            arr[preindex+1] = arr[preindex]
            preindex -=1
        # 找到位置并插入现在的值
        arr[preindex+1] = current