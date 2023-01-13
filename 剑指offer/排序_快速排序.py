"""
1.从数列中挑出一个元素，称为 “基准”（pivot）；
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
#处理大数据最快的排序算法之一了
"""


def partitino(arr, low, high):
    i = low - 1  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    # low:起始索引
    # high:结束索引
    if low < high:
        pi = partitino(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
