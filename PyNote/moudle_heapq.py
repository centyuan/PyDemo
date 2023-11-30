"""
堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。

最大堆 根结点的键值是所有堆结点键值中最大者，任意节点的值大于等于左右节点的值
最小堆 根结点的键值是所有堆结点键值中最小者，任意节点的值小于等于左右节点的值

heapq实:现了一个适合Python List一起使用的最小堆排序算法

方法:
heapq.nlargest(n,list)    # 最大n个
heapq.nsmallest(n,list)   # 最小n个
heapq.nsmallest(n,list,key=lambda: item: item["price"])  # 用于复杂的数据结构
heapq.heapify(list)       # 将list堆化 时间复杂度 O(n)

"""
