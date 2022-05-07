   #！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-5 下午7:54

# 1.__init__方法使用与功能：
    # 1.用来构造初始化函数, 用来给类的实例进行初始化属性，所以可以不需要返回值
    # 2.在创建类的实例时系统自动调用
    # 3.自定义类如果不定义的话，默认调用父类object的，同理继承也是，子类若无，调用父类，若有，调用自己的


class Student(object):
    def __init__(self, name):
        self.name = name
        print("1.这是__init__方法")


s = Student("tom")
'''
这是__init__方法
'''

# 2.__new__方法使用与功能
    # 1.__new__功能：用所给类创建一个对象，并且返回这个对象。
    # 2.因为是给类创建实例，所以至少传一个参数cls, 参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
    # 3.在类实例化时内部创建类实例的函数，并且返回这个实例，所以它是类实例时最先被调用的方法，一般不要人为定义该方法。
    # 4.因为要创建实例返回实例，所以要有返回值。return父类__new__出来的实例，或者直接是object的__new__出来的实例


class Student(object):
    def __init__(self, name):
        self.name = name
        print("2.这是__init__方法")

    def __new__(cls, *args, **kwargs):
        print("2.这是__new__方法")
        return object.__new__(cls)


s = Student("tom")
'''结果如下：注意__new__的执行顺序在__init__之前
这是__new__方法
这是_init__方法
'''

# 3.__init__和__new__使用的联系
# 1.__init__第一个参数是self，表示需要初始的实例，由python解释器自动传入，而这个实例就是这个__new__返回的实例
# 2.然后 __init__在__new__的基础上可以完成一些其它初始化的动作

class Student(object):
    def __init__(self, name):
        self.name = name
        print("3.这是__init__方法")

    def __new__(cls, *args, **kwargs):
        print("3.这是__new__方法")
        id = object.__new__(cls)
        print('__new__:',id)  # 打印这个__new__创建并返回的实例在内存中的地址
        return id


s1 = Student("JACK")
print('s1:',s1)
'''
这是__new__方法
<__main__.Student object at 0x000001EC6C8C8748>
这是__init__方法
<__main__.Student object at 0x000001EC6C8C8748>
'''
#总结：很明显，这两个实例的内存地址一样，所以__init__接受的实例就是__new__创建的。
