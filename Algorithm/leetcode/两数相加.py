"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
2 4 3
5 6 4
7 0 8
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1.迭代法
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1.当前指针和结果链表
        result = current = ListNode()
        # 2.进位项
        remainder = 0
        # 3. 非空
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l1.val if l2 else 0
            total = x + y + remainder
            # 4.添加新节点,取余,个位数
            current.next = ListNode(total % 10)
            # 取整,
            remainder = total // 10
            # 5.移动到下一指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
        # 6.走到头还有remainder
        if remainder:
            current.next = ListNode(remainder)
        return result.next

    # 2.递归法
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = l1.val + l2.val
        # 1.向下进一位
        remainder = total // 10
        # 2.本节点
        res = ListNode(total % 10)
        if l1.next or l2.next or remainder:
            # 向下移动一位
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val = l1.val + remainder
            res.next = self.addTwoNumbers1(l1, l2)
        return res
