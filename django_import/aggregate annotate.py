"""
https://zhuanlan.zhihu.com/p/50974992
aggregate: 聚合函数

annotate: 注释的意思 更好的理解是分组
如果你想要对数据集先进行分组然后再进行某些聚合操作或排序时，需要使用annotate方法来实现


class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobbies = models.ManyToManyField(Hobby)

class Hobby(models.Model):
    name = models.CharField(max_length=20)


# 1.求学生的平均年龄
from django.db.models import Avg,Max,Min,Count

    Student.objects.all().aggregate(Avg('age'))
all()不是必须的。或者
    Student.objects.aggregate(Avg('age'))
返回: {'age_avg':12}

# 2. 求学生最大年龄,最小年龄
    Student.objects.aggregate(Max('age'),Min('age'))
返回: {'age_max':18,'age_min':6,}

# 3. 根据Hobby表反查学生最大年龄，student和age间有双下划线
    Hobby.object.aggregate(Max('student__age'))

###############################################################
# 4. 按学生分组，统计每个学生的爱好数量
    Student.objects.annotate(Count('hobbies'))
    Student.objects.annotate(hobbies=Count('hobbies')) # 指定返回名字 hobbies
返回的结果依然是Student查询集，只不过多了hobbies__count这个字段

# 5. 按爱好分组，在统计每组学生数量
    Hobby.objects.annotate(Count('student'))

# 6. 按爱好分组，在统计每组学生最大年龄
    Hobby.objects.annotate(Max('student__age'))

# 7. 统计最受学生欢迎的5个爱好
    Hobby.objects.annotate(student_num=Count('student')).order_by('-student_num')[:5]

# 上面都是按学生对象分组,下面将按学生名字分组
# 8. 按学生名字分组，统计每个学生的爱好数量(名字相同的学生，爱好数量会叠加)
    Student.objects.values('name').annotate(Count('hobbies'))

# 8. 按学生名字，年龄分组
    Student.objects.values('name','age').annotate(Count('hobbies'),Max())



"""