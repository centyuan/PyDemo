# _*_ coding:utf-8 _*_
# @Author : centyuan
"""
这是我们需要用一个特殊的方法或机制要访问和操作这个未知的方法或变量，这中机制就称之为反射。接下记录下反射几个重要方法
"""


# hasattr 判断对象中是否有指定名字的属性或方法，返回bool
# getattr 获取对象中指定名词的属性或方法，返回str
# setattr 给指定对象添加属性或方法
# delattr 删除对象指定名词的属性或方法,无返回值

def abc():
    pass


class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("%s正在谈话" % (self.name))


p = Person("yuan")
print(hasattr(p, 'talk'))  # True
print(getattr(p, "name"))  # 获取name变量的值
print(getattr(p, 'talk'))
setattr(p, 'get_age', abc)  # 添加abc函数到中为get_age
setattr(p, 'age', 30)  # 添加age变量到类中
