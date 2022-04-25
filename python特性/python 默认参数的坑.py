# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-2 下午2:47

"""
python函数的几种参数可以任意组合，
但必须按顺序写，否则会报错，顺序为（  位置参数，默认参数，(可变长参数)可变参数，命名关键字参数，(可变长参数)关键字参数）

"""
# 参考:https://www.jianshu.com/p/a74442a18077?utm_campaign
# https://segmentfault.com/a/1190000013117996
# 位置参数,默认参数(默认参数必须指向不变对象,int string,tuple),可变参数(*args),命名关键字参数(*右边为),关键字参数(就是**kwargs）
# 在tuple或list前加一个*，构造出可变参数,在dict前加两个*，构造关键字参数。
# 命名关键字参数类似 默认参数
"""
def person(name,age,*,city,job):
    print(name,age,city,job)
#命名关键字参数，调用的时候必须传入参数名
person('Jack',24,city='Beijing',job='Engineer')
"""
"""
def  add_end(L=[]):
    L.append('END')
    return L
当你正常调用时，结果似乎不错：
add_end([1, 2, 3])
#[1, 2, 3, 'END']
add_end(['x', 'y', 'z'])
#['x', 'y', 'z', 'END']
当你使用默认参数调用时，一开始结果也是对的：

add_end()
#['END']
但是，再次调用add_end()时，结果就不对了：

add_end()
#['END', 'END']
add_end()
#['END', 'END', 'END']

#默认参数必须指向不变对象
要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
现在，无论调用多少次，都不会有问题：

>>> add_end()
['END']
>>> add_end()
['END']

"""
