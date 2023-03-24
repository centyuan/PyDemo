# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 16:25

import random
def foo(n):
    random.seed()
    c1 = 0
    c2 = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        r1 = x * x + y * y
        r2 = (1 - x) * (1 - x) + (1 - y) * (1 - y)
        if r1 <= 1 and r2 <= 1:
            c1 += 1
        else:
            c2 += 1
    return c1 / c2
print(foo(10))
sizes = ['S','M']

colors = ['white','black']

shirts = [(size,color) for color in colors for size in sizes]
shirts1 = [[1,2,3] for a in range(2)]
print(shirts,shirts1)