#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午5:39

# classmethod
# 必须有一个指向类对象的引用作为第一个参数，而
# staticmethod
# 可以没有任何参数

"""
在Python中，有以下几种方式来定义变量：
xx：公有变量
_xx：单前置下划线，被看作是“protect”化属性或方法，类对象和子类可以访问，from somemodule import *禁止导入
__xx：双前置下划线，被看作是"private”化属性或方法，无法在外部直接访问只能类对象访问（名字重整所以访问不到）
__xx__：双前后下划线，系统定义名字（不要自己发明这样的名字）
xx_：单后置下划线，用于避免与Python关键词的冲突
"""
"""
实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。
类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：类和实例对象都可以调用。
静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：类和实例对象都可以调用。
example:如有一个学生类和一个班级类
        功能:执行班级人数增加的操作、获得班级的总人数
        这个问题用类方法做比较合适，为什么？因为我实例化的是学生，
        但是如果我从学生这一个实例中获得班级总人数，在逻辑上显然是不合理的。
        同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的。
"""
class Num:
    var = "类变量"
    _variable = "类私有变量"
    __num = 0
    # 普通方法：能用Num调用而不能用实例化对象调用,
    def one():
        print('1')

    # 实例方法：能用实例化对象调用而不能用Num调用,调用的时候会将该对象参数自动传入
    def two(self):
        print('2')

    # 静态方法：能用Num和实例化对象调用,因为没有传入cls和self所以不能修改类属性,可以传入相应参数做修改
    # 静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，
    # 不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
    @staticmethod
    def three():
        print('3')

    # 类方法：能用Num和实例化对象调用,第一个参数cls长什么样不重要，都是指Num类本身，调用时将Num类作为对象隐式地传入方法
    @classmethod
    def go(cls):
        cls.__num +=1
        cls.three()


Num.one()  # 1
# Num.two()         #TypeError: two() missing 1 required positional argument: 'self'
Num.three()  # 3
Num.go()  # 3
print(dir(Num))
if not hasattr(Num,'var'):
    print("no")
else:
    print("yes")

i = Num() #类实例化
# i.one()           #TypeError: one() takes 0 positional arguments but 1 was given
i.two()  # 2
i.three()  # 3
i.go()