# -*- coding:utf-8 -*-
# __new__方法是创建类实例的方法, 创建对象时调用, 返回当前对象的一个实例
# __init__方法是类实例创建之后调用, 对当前对象的实例的一些初始化, 没有返回值

#python中进行面向对象编程，当在子类的实例中调用父类的属性时，
# 由于子类的__init__方法重写了父类的__init__方法，
# 如果在子类中这些属性未经过初始化，使用时就会出错。例如以下的代码:


class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__sex=None #私有变量只有内部可以访问，外部不能访问，
        """
        双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name
        是因为Python解释器对外把__name变量改成了_Student__name，
        所以，仍然可以通过_Student__name来访问__name变量：
        """

    def pr(self):
        pass
class Student(Human):

    def __init__(self,school,name,age):
        self.school=school
        #Human.__init__(self,name,age)#将值传递给父类
        super(Student,self).__init__(name,age) #子类调用父类
    def pr(self):
        print('子类')
        super(Student, self).pr() #子类调用父类

student1=Student('海南师范大学','genie','22')
print(student1.name)
print(student1.age)
student1.pr()

class A(object):
    def __init__(self):
        self.a = 5

    def function_a(self):
        print('I am from A, my value is %d' % self.a)


class B(A):
    def __init__(self):
        self.b = 10

    def function_b(self):
        print('I am from B, my value is %d' % self.b)
        self.function_a()    # 调用类A的方法，出错



# if __name__ == '__main__':
#     b = B()
#     b.function_b()

b=B()
b.function_a()#会报错AttributeError: 'B' object has no attribute 'a'
#解决方法2中：
#1调用未绑定的父类__init__方法
# def __init__(self):
#         A.__init__(self)   # 此处修改了。如果类A的__init__方法需要传参，也需要传入对应的参数
#         self.b = 10
#2调用super函数
# def __init__(self):
#         super(B, self).__init__()   # 此处修改了
#         self.b = 10
#方法一简单直观，但面对多继承问题，只能多次调用每个父类的__init__方法
# 方法二不太直观，但可以解决多继承问题，会一次性的执行所有的父类的对应方法


