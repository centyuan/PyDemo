# -*- coding:utf-8 -*-
class Student():
    name='123'
    age='123333'
    xuehao='hain'
    __xuexiao='海南师范大学'#私有变量
    #构造函数
    def __init__(self,name,age): #类变量,实例变量 (实例变量找不到会去类变量,父类变量里查找)
         self.name=name
         self.age=age
         self.suis='我的'
         print(Student.xuehao)#访问类变量 print(self.__class__.xuehoa)
         print(self.__class__.xuehao)
         print(Student.name)

    def print_info(self): #实例方法
        print(self.name,self.age,self.suis)
    @classmethod  #类方法 不能访问实例变量
    def print_i(cls):
        cls.xuehao+='123'
        print(cls.xuehao)
    @staticmethod #静态方法(没有传入self等参数)不能访问实例变量
    def print_a():
        pass
    def __nihao(self):#私有函数
        pass


student1=Student('张三','李四')
#print(student1.name)
#print(student1.age)
student1.print_info()
print(Student.name,Student.age)
print(Student.__dict__)
print(student1.__dict__)
Student.print_i()
student1.print_i()#最好不要
#报错不能外部访问print(Student.__xuexiao)
#Student.__xuexiao=123 会给类添加一个新的变量病赋值而不是访问原来的
#print(Student.__xuexiao)

