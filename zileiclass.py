# -*- coding:utf-8 -*-
from fuleiclass import Human

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

