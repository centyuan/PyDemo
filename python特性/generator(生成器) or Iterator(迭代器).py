#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午8:34


#迭代器：iter()和next()

list = [1,4,6,7]
it = iter(list) #创建迭代器对象
# for n in range(len(list)):
#     print(next(it))
for x in it:  #迭代器直接遍历 不用next()
    print(x,end=' ')

"""
在Python中，这种一边循环一边计算的机制，称为生成器：generator
使用yield的函数被称为生成器(生成器是一个返回迭代器对象的函数,简单来说生成器就是一个迭代器)
每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
"""
#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b # 遇到yield返回,再次执行时从这继续
        a,b = b,a+b
        n = n+1
    return 'done'

for n in fib(6): # f=fib(6)是一个迭代器，有生成器返回
    print('函数形式生成器:',n)
for n in range(7):
    next()
# 推导式:
L = [x*x for x in range(10)] # 列表生成式或列表推导式
g = (x*x for x in range(10)) # 简单的创建生成器
for item in g:
    print('列表：',item)


"""
next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
isinstance(variable,Iterator)来判断是否是迭代器对象
生成器都是Iterator对象,
list、dict、str虽然是Iterable，却不是Iterator
把list、dict、str等Iterable变成Iterator可以使用iter()函数
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
Python的for循环本质上就是通过不断调用next()函数实现的
迭代器就是不但可以作用于for循环，还可以被next()不断的调用并返回下一个值，
直到最后抛出一个错误StopIteration错误，表示无法继续返回下一个值。

"""
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break