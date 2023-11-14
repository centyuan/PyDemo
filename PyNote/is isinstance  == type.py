# -*- coding:utf-8 -*-
# Author centyuan


# 获取类的名字
class ShowHello(object):
    def __init__(self, name):
        self.name = name

    def my_name(self):
        print("{1}-class_name::{0}".format(type(self).__name__, self.name))


"""
is运算符比==速度快
==:比较的是两个对象的值
is:比较的是两个对象是否是同对象(不会考虑子类)
isinstance:判断两个类型是否相同(isinstance),类似 type
diff:
    type:不会认为子类是一种父类类型，不考虑继承关系
    isinstance:会认为子类是一种父类类型，考虑继承关系

如果使用== 对两个对象进行比较的话，即使是同一个对象，也会把对象的值再进行一次比较（此步骤对于同一个对象来说是多余的）,
使用is比较两对象的话，只需要判断两个对象是否为同一个即可，当判断一个对象的类型时，使用is的效果会比 ==更好一些。

first:在 Python 中会实现创建一个小型的整形池，范围为 [-5,256]，为这些整形开辟好内存空间，当代码中定义该范围内的整形时，不会再重新分配内存地址
seconde:后来查了资料才发现是：Python出于对性能的考虑，但凡是不可变对象，在同一个代码块中的对象，只有是值相同的对象，就不会重复创建，而是直接引用已经存在的对象。

"""

if __name__ == "__main__":
    hello = ShowHello("python")
    h2 = hello
    hello.my_name()
    print(isinstance(ShowHello, object))  # 会认为子类是一种父类类型，考虑继承关系
    print(isinstance(hello, ShowHello))
    print(isinstance(hello, object))
    print(hello is ShowHello)
    print(hello is h2)
