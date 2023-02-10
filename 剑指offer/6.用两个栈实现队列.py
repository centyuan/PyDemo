# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
借助栈的先进后出规则模拟实现队列的先进先出
1、当插入时，直接插入 stack1
2、当弹出时，当 stack2 不为空，弹出 stack2 栈顶元素，如果 stack2 为空，将 stack1 中的全部数逐个出栈入栈 stack2，再弹出 stack2 栈顶元素
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()  # 默认最后一个元素
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
