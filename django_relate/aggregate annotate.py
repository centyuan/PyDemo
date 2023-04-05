"""
https://zhuanlan.zhihu.com/p/50974992
aggregate: 聚合函数
annotate: 注释的意思 更好的理解是分组,如果你想要对数据集先进行分组然后再进行某些聚合操作或排序时，需要使用annotate方法来实现
"""
from django.db import models


class Hobby(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobbies = models.ManyToManyField(Hobby)


# 一:aggregate
from django.db.models import Avg, Max, Min, Count, Sum

# 1.求学生的平均年龄
Student.objects.all().aggregate(Avg('age'))
Student.objects.aggregate(Avg('age'))  # {'age_avg':12}
Student.objects.aggregate(age_avg=Avg("age"))

# 2. 求学生最大年龄,最小年龄
Student.objects.aggregate(Max('age'), Min('age'))  # 返回: {'age_max':18,'age_min':6,}

# 3. 根据Hobby表反查学生最大年龄，student和age间有双下划线
Hobby.object.aggregate(Max('student__age'))

# 二:annotate
# 1. 按学生分组，统计每个学生的爱好数量
# 返回的结果依然是Student查询集，只不过多了hobbies__count这个字段
Student.objects.annotate(Count('hobbies'))
Student.objects.annotate(hobbies=Count('hobbies'))  # 指定返回名字 hobbies

# 2. 按爱好分组，在统计每组学生数量
Hobby.objects.annotate(Count('student'))

# 3. 按爱好分组，在统计每组学生最大年龄
Hobby.objects.annotate(Max('student__age'))

# 4. 统计最受学生欢迎的5个爱好,多一个student_num字段
Hobby.objects.annotate(student_num=Count('student')).order_by('-student_num')[:5]

# 5. 按学生名字分组，统计每个学生的爱好数量(名字相同的学生，爱好数量会叠加)
Student.objects.values('name').annotate(Count('hobbies'))

# 6. 按学生名字，年龄分组
Student.objects.values('name', 'age').annotate(Count('hobbies'), Max())

# 7.按月份统计数据
from django.db.models.functions import TruncMonth

# 按照月份分组算出各个月份的合同金额总和
queryset = None
query = queryset.annotate(month=TruncMonth('created_at')).values('month').annotate(
    contract_amount=Sum('contract_amount')
)
# 8.加上时间范围如下: 算出时间在created_range在这之间月份的每月合同金额总和
created_range = ['2019-11-11', '2019-12-12']
queryset.annotate(month=TruncMonth('created_at')).filter(month__range=created_range).annotate(
    contract_amount=Sum('contract_amount'))

# 9.算某月的总和, 利用aggregate, 并且制定时间, 这里要注意month制定的是某个月的1号
queryset.annotate(month=TruncMonth('created_at')).filter(month='2019-11-01').aggregate(
    contract_amount=Sum('contract_amount'))

# Django F对象和Q对象查询详解
# http://c.biancheng.net/view/7693.html
