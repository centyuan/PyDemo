"""
1.从数列中挑出一个元素，称为 “基准”（pivot）；
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
#处理大数据最快的排序算法之一了
时间复杂度:O(n log n),最糟情况为O(n平方)
快速排序的性能高度依赖于你选择的基准值
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


def quick_sort2(arr):
    if len(arr) < 2:
        # 基线条件,为空或只包含一个元素的数组是有序的
        return arr
    else:
        pivot = arr[0]  # 递归条件
        # 所有小于基准值
        less = [i for i in arr[1:] if i < pivot]
        # 所有大于基准值
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort2(less) + [pivot] + quick_sort2(greater)


if __name__ == '__main__':
    arr = [1, 20, 9, 2, 31, 10000, 5, 7, 28, 30, 39, 100, 120, 99]
    a = quick_sort2(arr)
    print(a)
