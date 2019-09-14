#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午3:18

"""
type有两种用法：
1获取对象类型
2动态的创建类：
type(类名,父类的元组(针对继承的情况，可以为空),包含属性的字典(名称和值))

python 元类和描述符
"""

#一：描述符（和@property类似，可以避免写很多装饰器而显得累赘）
#：描述符就是一个“绑定行为“的对象属性，在描述符协议中，它可以通过方法充写属性的访问。
# 这些方法有get(),set(),delete().如果这些方法中任何一个被定义在一个对象中，这个对象就是一个描述符

#参考:https://www.cnblogs.com/Jimmy1988/p/6808237.html
class Product():

    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if value < 0:
            raise ValueError('quantity must be >= 0')
        else:
            self._quantity = value

book = Product('mybook',6,30)
print(book.quantity)
print(dir(book))


class NotNegative():

    def __init__(self,name):
        self.name = name

    def __get__(self, instance, owner):
        return  self.name

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(self.name + ' must be >= 0')
        else:
            instance.__dict__[self.name] = value

class Product1():
    quantity = NotNegative('quantity')
    price = NotNegative('price')

    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

book = Product1('mybook',2,5)
print(book.quantity)



class Desc(object):
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('='*40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('='*40, "\n")


class TestDesc(object):
     x = Desc()
t =TestDesc()
t.x
t.x =2
