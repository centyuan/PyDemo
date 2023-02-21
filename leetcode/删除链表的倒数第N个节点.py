"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # 1.递归+回溯(走到结尾,回溯从0计数,到n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        global i
        if head is None:
            i = 0
            return
        head.next = self.removeNthFromEnd(head.next, n)
        i += 1
        return head.next if i == n else head

    # 2.快慢指针(fasts先走n步,在同时走,slow始终比fast慢n,直到fast结尾)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummpy = ListNode(0)
        slow = fast = dummpy
        dummpy.next = head
        # 1.先走n步
        for _ in range(n):
            fast = fast.next
        # 2.同时走
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        # 3.删除节点
        slow.next = slow.next.next
        return dummpy.next