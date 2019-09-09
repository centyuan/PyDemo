#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-8 下午8:06
"""
堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。

最大堆 根结点的键值是所有堆结点键值中最大者。

最小堆 根结点的键值是所有堆结点键值中最小者。
"""

class heap(object):
    def __init__(self):
        # 初始化一个空堆，使用数组来在存放堆元素，节省存储
        self.data_list = []

