# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-6 下午8:00

class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):  # 进栈
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")  # 空栈不能pop

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


# 例子1：使用堆栈检查括号字符串是否平衡
# 举例：
#
# ((())): True
#
# ((()): False

# 循环遇到'('进栈,遇到')'出栈，最好判断栈是否为空
def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
