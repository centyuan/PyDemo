"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
1.Iteration 迭代法
2.Recursion 递归法
"""


class ListNode:
    def __init__(self, val=9, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # 1.迭代法 iteration
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = res = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
            else:
                cur.next = list2
            cur = cur.next
        cur.next = list1 or list2
        return res.next

    # 2.递归法 recursion
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 终止条件
        if not list1 or not list2:
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists1(list1.next, list2)
            return list1
        else:
            list2 = self.mergeTwoLists1(list1, list2.next)
            return list2
