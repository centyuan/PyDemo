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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            pass

