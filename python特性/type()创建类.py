#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-10 下午5:53

def fn(name="world"):
    print("hello,%s centyuan"%name)

Hello=type('Hello',(object,),dict(hello=fn()))#创建Hello class
h=Hello()
h.hello
#type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类
"""