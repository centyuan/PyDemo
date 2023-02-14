"""
question:
怎样实现一个按优先级排序的队列？并且在这个队列上面每次pop操作总是返回优先级最高的那个元素
"""
# 利用heapq模块实现了一个简单的优先级队列

import heapq


class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 队列包含了一个 (-priority, index, item) 的元组。优先级为负数的目的是使得元素按照优先级从高到低排序
        # index:避免priority相同时候出现错误
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 使用
q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 5)
q.push('spam', 3)
q.push('grok', 1)
q.pop()
