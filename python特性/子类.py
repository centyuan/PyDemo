#!/usr/bin/python
# -*- coding:utf-8 -*-
# 寻找属性和方法的顺序问题：先从对象自己的命名空间中找，然后在自己的类中，最后在从父类当中去找
#类变量 实例变量
class Student():

    #在类内部定义的属性属于类本身的,由操作系统只分配一块内存空间,大家公用这一块内存空间。
    count = 2
    count1 = 3
    name = 1
    namestr = 'namestr'
    gender = 'man'
    def __init__(self,name,age):
        print("before Student.__init__ name:", name, self.name)
        self.name = name
        print("after Student.__init__ name:", name, self.name)
        self.age = age
        Student.count +=1
        #self.count1 +=1
        Student.count1 +=1
        #self.name={2:2}
        #self.namestr='efg123x'
        self.gender=self.gender
        print("Student.__init__ gender", self.gender)
        print("Student.__init__ namestr", self.namestr)
        print("Student.__init__ Student.count,Student.count1：", self.count,self.count1)
        print(self.count, self.count1)

class Data_test2(object):
    day=0
    month=0
    year=0
    def __init__(self,year=0,month=0,day=0):
        self.day=day
        self.month=month
        self.year=year

    @classmethod
    def get_date(cls,data_as_string):
        #这里第一个参数是cls， 表示调用当前的类名
        year,month,day=map(int,data_as_string.split('-'))
        date1=cls(year,month,day)
        #返回的是一个初始化后的类
        return date1

    def out_date(self):
        print("year :")
        print(self.year)
        print("month :")
        print(self.month)
        print("day :")
        print(self.day)

if __name__ == '__main__':
    student1 = Student("lidong",25)
    print("student1.__dict__:", student1.__dict__)
    student2 = Student("wangwu",28)
    print(student2.__dict__)
    print("student2.count:", Student.count)
    print("student2.count:", Student.count1,end='--')
    print(Student.namestr)
    print(id(Student.name))
    print(student1.namestr)
    print(student1.name)
    print(id(student1.name))
    print(student2.namestr)
    print(id(student2.name))
    #print(Student.age)
    print(student1.age)
    print(student2.age)
    print(Student.__dict__)


