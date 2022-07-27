# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 21:35
"""
在做程序开发中，我们常常会遇到这样的需求：需要执行对象里的某个方法，或需要调用对象中的某个变量，
但是由于种种原因我们无法确定这个方法或变量是否存在，
这是我们需要用一个特殊的方法或机制要访问和操作这个未知的方法或变量，这中机制就称之为反射。接下记录下反射几个重要方法
"""
# hasattr 判断对象中是否有这个方法或变量
# getattr 获取对象中的方法的内存地址或变量的值
# setattr 为对象添加变量或方法
# delattr

def abc():
    pass
class Person(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("%s正在谈话"%(self.name))

p = Person("yuan")
print(hasattr(p,'talk')) # True
print(getattr(p,"name"))  #获取name变量的值
print(getattr(p,'talk'))
setattr(p,'get_age',abc) # 添加abc函数到中为get_age
setattr(p,'age',30) #添加age变量到类中