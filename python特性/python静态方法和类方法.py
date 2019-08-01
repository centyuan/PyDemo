#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午5:39

# classmethod
# 必须有一个指向类对象的引用作为第一个参数，而
# staticmethod
# 可以没有任何参数


class Num:
    # 普通方法：能用Num调用而不能用实例化对象调用,
    def one():
        print('1')

    # 实例方法：能用实例化对象调用而不能用Num调用,调用的时候会将该对象参数自动传入
    def two(self):
        print('2')

    # 静态方法：能用Num和实例化对象调用,因为没有传入cls和self所以不能修改类属性,可以传入相应参数做修改
    #主要是方便将外部函数集成到类体中,美化代码结构,重点在不需要类实例化的情况下调用方法
    @staticmethod
    def three():
        print('3')

    # 类方法：能用Num和实例化对象调用,第一个参数cls长什么样不重要，都是指Num类本身，调用时将Num类作为对象隐式地传入方法
    @classmethod
    def go(cls):
        cls.three()


Num.one()  # 1
# Num.two()         #TypeError: two() missing 1 required positional argument: 'self'
Num.three()  # 3
Num.go()  # 3

i = Num() #类实例化
# i.one()           #TypeError: one() takes 0 positional arguments but 1 was given
i.two()  # 2
i.three()  # 3
i.go()