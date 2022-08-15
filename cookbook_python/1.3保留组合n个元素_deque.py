"""
q = deque(maxlen=3) # 会新建一个固定大小的队列，当新的元素加入并且队列满的时候，最老的元素自动被移除
q.append(1)
#不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添加和弹出元素的操作
q.appendleft(1) # 左边添加
q.popleft(1)    # 左边弹出

"""
from collections import deque

# 在队列两端插入或删除元素时间复杂度都是O(1)，而在列表的开头插入或删除元素的时间复杂度为O(N)
q = deque(maxlen=10)
q.append(1)
q.append(2)
q.pop()
print(q)
q.appendleft(0)
q.popleft()
