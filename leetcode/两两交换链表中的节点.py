"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""


class LiseNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # 1.迭代
    def swapPairs(self, head: Optional[LiseNode]) -> Optional[LiseNode]:
        if head == None or head.next == None:
            return head
        cur = res = LiseNode()
        res.next = head
        while cur.next != None and cur.next.next != None:
            # 1.分别记住第二,第三
            nxt = head.next
            temp = nxt.next
            # 2.交换
            cur.next = nxt
            nxt.next = head
            head.next = temp
            # 3.cur,head分别向右移动两位
            cur = head
            head = head.next
        return res.next

    # 2.递归
    def swapPairs(self, head: Optional[LiseNode]) -> Optional[LiseNode]:
        if head == None or head == None:
            return head
        nxt = head.next
        head.next = self.swapPairs(nxt.next)
        next.next = head
        return nxt
