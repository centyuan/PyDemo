"""
q = deque(maxlen=3)
会新建一个固定大小的队列，当新的元素加入并且队列满的时候，最老的元素自动被移除
不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添加和弹出元素的操作
"""
from collections import deque

# 在队列两端插入或删除元素时间复杂度都是O(1)，而在列表的开头插入或删除元素的时间复杂度为O(N)
q = deque(maxlen=10)
# 右边
q.append(1)             # 右边添加一个元素
q.pop()                 # 右边弹出一个元素
q.extend([1,2,3])       # 右边添加一组元素
print(q)
# 左边
q.appendleft(0)         # 左边添加一个元素
q.popleft()             # 左边弹出一个元素
q.extendleft([1,2,3])   # 左边添加一组元素
# 实现加操作等价于.extend()
q +=['a','b','c']
print("q:",q)