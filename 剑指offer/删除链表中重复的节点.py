#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-22 下午6:01
"""题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
class ListNode:
 def __init__(self, x):
      self.val = x #
      self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                    last.next = curr
        return first.next
