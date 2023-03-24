"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
from typing import Optional


class LiseNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1.迭代
    def reverseList(self, head: Optional[LiseNode]) -> Optional[LiseNode]:
        preNode = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = preNode
            preNode = cur
            cur = nxt
        return cur

    # 2.递归
    def reverseList2(self, head: Optional[LiseNode]) -> Optional[LiseNode]:
        if not head or not head.next:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last
