"""
1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3.针对所有的元素重复以上的步骤，除了最后一个；
4.重复步骤1~3，直到排序完成
时间复杂度:O(n平方), 稳定
"""


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        # 没有提前结束
        if flag:
            break
    return arr
