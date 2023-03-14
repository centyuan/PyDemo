"""
给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""

# 1.暴力,循环A循环B
# 2.哈希
# 3.双指针
# a+c=m,b+c=n,=>a+c+b = b+c+a
# d = m-n,=>d=a-b
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        m, n = 0, 0
        while headA:
            m += 1
            headA = headA.next
        while headB:
            n += 1
            headB = headB.next
        d = m-n
        while d:
            pass