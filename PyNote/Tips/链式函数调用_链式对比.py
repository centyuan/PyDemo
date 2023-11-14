# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:26

# 1.链式函数调用
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5
print((subtract if a > b else add)(a, b))

# 2. 链式对比
a = 2
print(2 < a < 8)  # True
print(1 == a < 3)  # False
