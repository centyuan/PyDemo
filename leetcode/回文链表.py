"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1.双指针+数组
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        n = len(vals)
        for i, v in enumerate(vals[:n // 2]):
            if v != vals[n - 1 - i]:
                return False
        return True

    # 2.双指针+反转链表()
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while not fast and not fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverseList(slow)
        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverseList(self, head):
        preNode = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = preNode
            preNode = cur
            cur = nxt
        return preNode
