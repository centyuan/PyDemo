# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

"""
python函数的几种参数可以任意组合，
但必须按顺序写，否则会报错，顺序为（位置参数，默认参数，(可变长参数)可变参数，命名关键字参数，(可变长参数)关键字参数）

"""


# 参考:https://www.jianshu.com/p/a74442a18077?utm_campaign
# 位置参数,默认参数(默认参数必须指向不变对象,int string,tuple),可变参数(*args),命名关键字参数(*右边为),关键字参数(就是**kwargs）
# 在tuple或list前加一个*，构造出可变参数,在dict前加两个*，构造关键字参数。
# 命名关键字参数类似 默认参数

# 1. 命名关键字参数

def person(name, age, *, city, job):
    print(name, age, city, job)


# 命名关键字参数，调用的时候必须传入参数名
person('Jack', 24, city='Beijing', job='Engineer')

# 2.默认参数为可变对象时，有如下问题
"""
def  add_end(L=[]):
    L.append('END')
    return L
    
# 调用传参
add_end([1, 2, 3])
#[1, 2, 3, 'END']
add_end(['x', 'y', 'z'])
#['x', 'y', 'z', 'END']

# 调用不传参数，使用默认参数时
# 用默认参数调用时，一开始结果也是对的：
add_end()  #['END']
# 但是，再次调用add_end()时，结果就不对了：
add_end()  #['END', 'END']
add_end()  #['END', 'END', 'END']


# 解决方案(默认参数必须指向不变对象，要修改上面的例子，我们可以用None这个不变对象来实现)
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 无论调用多少次，都不会有问题

add_end()  #['END']
add_end()  #['END']

"""


# 3. 位置参数问题终结解释
# Python的默认参数只在函数定义时被赋值一次，而不会每次调用函数时又创建新的引用。这意味着，函数定义完成后，默认参数已经存在固定的内存地址了，
# 如果使用一个可变的默认参数并对其进行改变，那么以后对该函数的调用都会改变这个可变对象，而默认参数如果是不可变对象(None,True|Fales,数字,或字符串)，不存在该问题，
def fun(a=(), b=[]):
    a += (1,)
    print(a)
    b.append(1)
    print(b)
    return a, b


fun()
print(fun())
# 输出((1,), [1, 1])
