# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午8:34

# 一：迭代器
it = iter([1, 2, 3, 4, 5])  # 创建迭代器对象

# 1.迭代器直接遍历 不用next()
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
# 2.迭代器直接遍历 不用next()
for x in it:
    print(x, end=' ')

# 二：生成器
"""
在Python中，这种一边循环一边计算的机制，称为生成器：generator
使用yield的函数被称为生成器(生成器是一个返回迭代器对象的函数,简单来说生成器就是一个迭代器)
每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
"""


# 1. yield创建生成器
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 遇到yield返回,再次执行时从这继续
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):  # f=fib(6)是一个迭代器，有生成器返回
    print('函数形式生成器:', n)

# 2.推导式创建生成器:
# L = [x * x for x in range(10)]  # 列表生成式或列表推导式
g = (x * x for x in range(10))  # 简单的创建生成器
for item in g:
    print('列表：', item)
# next(g)   # next 取值
"""
Python的for循环本质上就是通过不断调用next()函数实现的
生成器取值：for循环，next()不断的调用
迭代器取值: for while循环

生成器都是Iterator对象:
1.list、dict、str虽然是Iterable，却不是Iterator
2.把list、dict、str等Iterable变成Iterator可以使用iter()函数
3.凡是可作用于for循环的对象都是Iterable类型；

"""
