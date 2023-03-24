#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan


"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

解题思路:
先从头遍历链表，再将列表翻转

"""

class ListNode():

    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:

    def printListFormTailToHead(self,listNode):
        val_list =[]
        node = listNode
        while node:
            val_list.append(node.val)
            node = node.next
        return val_list[::-1] #翻转链表

