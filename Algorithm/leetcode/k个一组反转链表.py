"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # 迭代
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != head:
            # 1. 改变方向
            nxt = p
            p.next = prev
            # 2.移动一位
            prev = p
            p = nxt
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1.
        hair = ListNode(0)
        hair.next = head
        pre = hair
        # 2.head存在
        while head:
            # 3.从头开始:查看剩余部分长度是否大于k
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            # 4.反转子链表
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            # 5.子链表接回原链表
            pre.next = head
            tail.next = nxt
            # 6.移动
            pre = tail
            head = tail.next
        return hair.next
