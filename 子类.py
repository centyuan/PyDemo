#!/usr/bin/python
# -*- coding:utf-8 -*-
# 寻找属性和方法的顺序问题：先从对象自己的命名空间中找，然后在自己的类中，最后在从父类当中去找
#类变量 实例变量
class Student():

    #在类内部定义的属性属于类本身的,由操作系统只分配一块内存空间,大家公用这一块内存空间。
    count = 0
    count1=0
    name=1
    namestr='abc123'
    gender='gender'
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.count +=1
        #self.count1 +=1
        Student.count1 +=1
        #self.name={2:2}
        #self.namestr='efg123x'
        self.gender=self.gender
        print(self.gender)
        print(self.namestr)

if __name__ == '__main__':
    student1 = Student("lidong",25)
    print(student1.__dict__)
    student2 = Student("wangwu",28)
    print(student2.__dict__)
    print(Student.count)
    print(Student.count1,end='--')
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


