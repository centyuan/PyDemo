from collections import deque

"""
python标准库包含四种队列:
queue.Queue
asyncio.Queue
multiprocessing.Queue
collections.deque
"""
# collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型
# 相比list有更低的时间和空间复杂度,list.append 或 .pop(0)模拟栈的先进先出,会非常耗时,牵扯到移动列表里的所有元素
# deque既可以表示队列也可以表示栈

dq = deque(range(10), maxlen=10)  # maxlen 可容纳元素的数量
print(dq)   #    deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
# rotate(n) n，当n > 0 时，队列的最右边的n 个元素会被移动到队列的左边。当n < 0 时，最左边的n 个元素会被移动到右边。
print(dq.rotate(3), dq)  #   deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
print(dq.rotate(-4), dq)  #     deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
#  appendleft(-1)
print(dq.appendleft(-1), dq)  # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
#  extend([10,20,30,40])
print(dq.extend([10, 20, 30, 40]),dq)    #  deque([4, 5, 6, 7, 8, 9, 10, 20, 30, 40], maxlen=10)
# extendleft(iter)方法会把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里的元素会逆序出现在队列里
print(dq.extendleft([10, 20, 30, 40]),dq)  #  deque([40, 30, 20, 10, 4, 5, 6, 7, 8, 9], maxlen=10)

"""
1:还有popleft等类似方法:是为了实现这些方法，双向队列也付出了一些代价，从队列中间删除元素的操作会慢一些，因为它只对在头尾的操作进行了优化
2:append 和popleft 都是原子操作，也就说是deque 可以在多线程程序中安全地当作先进先出的栈使用，而使用者不需要担心资源锁的问题
"""