#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-10-19 下午4:44

"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

ways:
stack_A保存插入到数据，出栈时，如果stack_B不为空，直接弹出，为空则把stack_A中的数据全部弹出放到stack_B中
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self,node):
        self.stack1.append(node)


    def pop(self):
        if self.stack2:
            return self.stack2.pop() #默认最后一个元素
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
