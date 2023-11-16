"""
question:
怎么从一个集合中获得最大或者最小的N个元素列表
heapq模块有两个函数：nlargest()和nsmallest()可以完美解决这个问题。
提供了很好的性能
"""
import heapq

# 1.基本
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('最大n个', heapq.nlargest(3, nums))
print('最小n个', heapq.nsmallest(3, nums))

# 2.复杂
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])  # 最贵的三个
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(expensive,cheap)
# 1.查找唯一的最小或最大（N=1）的元素的话，那么使用min()和max()函数会更快些。
# 2.查找的元素个数相对比较小的时候， heapq.nlargest() heapq.nsmallest()很适合
# 3.如果N的大小和集合大小接近的时候，先排序这个集合然后再使用切片操作会更快点（sorted(items)[:N]或者是sorted(items)[-N:]
