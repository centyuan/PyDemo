#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午5:39

# classmethod
# 必须有一个指向类对象的引用作为第一个参数，而
# staticmethod
# 可以没有任何参数


class Num:
    # 普通方法：能用Num调用而不能用实例化对象调用
    def one():
        print('1')

    # 实例方法：能用实例化对象调用而不能用Num调用
    def two(self):
        print('2')

    # 静态方法：能用Num和实例化对象调用
    @staticmethod
    def three():
        print('3')

    # 类方法：第一个参数cls长什么样不重要，都是指Num类本身，调用时将Num类作为对象隐式地传入方法
    @classmethod
    def go(cls):
        cls.three()


Num.one()  # 1
# Num.two()         #TypeError: two() missing 1 required positional argument: 'self'
Num.three()  # 3
Num.go()  # 3

i = Num()
# i.one()           #TypeError: one() takes 0 positional arguments but 1 was given
i.two()  # 2
i.three()  # 3
i.go()