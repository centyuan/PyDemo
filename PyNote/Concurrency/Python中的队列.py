# 1.collections.deque
"""
deque是双端队列,可以用来实现栈stack和队列queue
相比list，deque拥有更低的时间和空间复杂度

appendleft():左边添加一个元素
extendleft():左边添加一组元素
append():
extend():
popleft():左边弹出一个元素
pop():
count():

"""

# 2.queue.Queue/threading.Queue
"""
适用于多线程，Queue已经包含了锁，所以可以通过它在线程间安全地共享数据


"""

# 3.multiprocessing.Queue
"""
适用于多进程，还要multiprocessing.SimpleQueue,multiprocessing.JoinableQueue

"""

# 4.asyncio.Queue
"""
适用于协程


"""
