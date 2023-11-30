"""
heapq
queue.PriorityQueue 
Redis Zset
"""
# heaq:多个线程使用时，需要增加适当的锁和信号量机制

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self.index, item))
        # -priority:优先级为负数使元素按照优先级从高到底排序，优先级相同，可以使用index插入顺序来排序
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False


# queue.PriorityQueue：数字越小优先级越高,提供了同步和锁操作，支持并发的生产者和消费者
from queue import PriorityQueue as PQ

pq = PQ()
pq.put((1, "a"))
pq.put((2, "b"))
pq.put(item)
pq.get()
pq.qsize()
pq.empty()
