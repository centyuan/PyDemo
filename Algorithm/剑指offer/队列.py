# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-7 下午7:16

class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None  # 头部节点
        self.rear = None  # 尾部节点

    def is_empty(self):
        return self.head is None

    # 从队列尾部添加元素
    def enqueue(self, elem):
        p = Node(elem)  # 初始化一个新的节点
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    # 删除头部元素
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            result = self.head.elem
            self.head = self.head.next
            return result

    # 查看队列头部的元素
    def peek(self):
        if self.is_empty():
            print('not found')
        else:
            return self.head.elem

    def print_queue(self):
        print("queue:")
        temp = self.head
        myqueue = []
        while temp:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


# 队列之数组实现
class Queue():
    def __init__(self):
        self.entries = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度
        self.front = 0  # 表示队列头部位置

    def enqueue(self, item):
        self.entries.append(item)  # 添加元素到队列里面
        self.length = self.length + 1  # 队列长度增加 1

    def dequeue(self):
        self.length = self.length - 1  # 队列的长度减少 1
        dequeued = self.entries[self.front]  # 队首元素为dequeued
        self.front -= 1  # 队首的位置减少1
        self.entries = self.entries[self.front:]  # 队列的元素更新为退队之后的队列
        return dequeued

    def peek(self):
        return self.entries[0]  # 直接返回队列的队首元素


# 基于Queue的三种队列(先进先出,先进后出,优先级队列)
from queue import Queue, LifoQueue, PriorityQueue

Fifo_queue = Queue()
Lifo_queue = LifoQueue()
Priority_queue = PriorityQueue()
Priority_queue.put((1, '数据'))  # （优先级,数据）
