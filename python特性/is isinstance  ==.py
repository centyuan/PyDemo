# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/17 21:11

# 获取类的名字
class ShowHello(object):
    def __init__(self, name):
        self.name = name
    def my_name(self):
        print("{1}-class_name::{0}".format(type(self).__name__,self.name))
"""
== 比较的是两个对象的值
is 比较的是两个对象是否是同对象(不会考虑子类)
isinstance 判断一个对象的类型是否在元组中的对象中(isinstance() 会认为子类是一种父类类型，考虑继承关系。)

如果使用== 对两个对象进行比较的话，即使是同一个对象，也会把对象的值再进行一次比较（此步骤对于同一个对象来说是多余的）,
使用is比较两对象的话，只需要判断两个对象是否为同一个即可，当判断一个对象的类型时，使用is的效果会比 ==更好一些。
"""




if __name__ == "__main__":
    hello = ShowHello("python")
    h2 = hello
    hello.my_name()
    print(isinstance(ShowHello, object)) # 会认为子类是一种父类类型，考虑继承关系
    print(isinstance(hello, ShowHello))
    print(isinstance(hello, object))
    print(hello is ShowHello)
    print(hello is h2)



