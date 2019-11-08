#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午8:34

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。

在Python中，这种一边循环一边计算的机制，称为生成器：generator

isinstance(variable,generator)
"""
# 一:
L = [x*x for x in range(10)] # 列表生成式或列表推导式

g = (x*x for x in range(10)) # 简单的创建生成器
for item in g:
    print(item)

# 打印:next(g)或for item in g:generator也是可迭代对象

# 二:函数形式生成器
# 如果函数定义中包含yield关键字,那么这个函数就不再是普通函数,而是一个generator
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b # 遇到yield返回,再次执行时从这继续
        a,b = b,a+b
        n = n+1
    return 'done'

for n in fib(6):
    print(n)


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