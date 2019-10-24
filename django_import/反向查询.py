#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-2 下午8:15
from django_import.shortcuts import HttpResponse, render, redirect
from django_import.db import models


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    cdata = models.DateField()

    def __str__(self):
        return "%s" % [self.__class__, self.cname]


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)

    # 一对多
    # cid = models.ForeignKey(to="Class",to_field="id",related_name="student")
    cid = models.ForeignKey(to="Class", to_field="id")

    # 一对一
    detail = models.OneToOneField("StudentDetail", to_field="id")
    # 等同于如下的代码
    # detail = models.ForeignKey(to="StudentDetail",to_field="id",unique=True)

    def __str__(self):
        return "%s" % [self.sname]
class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.PositiveIntegerField()
    email = models.EmailField()
    memo = models.CharField(max_length=128)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField(to="Class",name="teacher")

#一对多操作 cid = models.ForeignKey(to="Class",to_field="id",related_name="student")
#一对一操作 detail = models.OneToOneField("StudentDetail", to_field="id")

#一对一操作：
# 正向查询
stu = models.Student.objects.first()
stu.detail.email
# 反向查询
detail = models.StudentDetail.objects.get(id=1)
detail.student.sname

#一对多操作：
#正向查询
stu = models.Student.objects.first()
stu.cid.cname

#反向查询
cls = models.Class.objects.first()
cls.student_set.all()