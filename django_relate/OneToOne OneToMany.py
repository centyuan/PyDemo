# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/27 18:49

from django.db import models


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    cdate = models.DateField()

    def __str__(self):
        return "%s" % [self.__class__, self.cname]

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50)
    # 一对一
    sdetail = models.OneToOneField("StudentDetail",to_field="id")

    # 一对多
    sclass = models.ForeignKey(to='Class',to_field='id')
    def __str__(self):
        return "%s" % [self.sname]



class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.PositiveIntegerField
    email = models.EmailField()
    memo = models.CharField(max_length=50)

# 一对一：
# 正向查询 由学生信息表查询学生详情表
stu = Student.objects.first()
stu.detail.email
# 反向查询 由学生详情表查询学生信息表
detail = StudentDetail.objects.get(id=1)
detail.student.sname

# 一对多：
# 正向查询:
stu = Student.objects.first()
stu.sclass.cname
# 反向查询：
cls = Class.objects.first()
cls.student_set.all()
# 如果不在外键的字段中设置related_name的话，默认就用表名_set。
# 如果设置了related_name=”students”，反向查询时可直接使用students进行反向查询。
cls.students.all()





