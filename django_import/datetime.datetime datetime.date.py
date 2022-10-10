# -*- coding:utf-8 -*-
# Author centyuan

from datetime import datetime
from django.db import models

# 1.日期
from django.utils.timezone import now,datetime,timedelta
print(datetime.now())  # 2019-10-28 10:41:27.201551
print(datetime.date(2019, 10, 28))  # 2019-10-28

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    add_time = models.CharField(default=datetime.now)
    date = models.DateField(auto_now_add=True)

    # auto_now_add  自动添加,以添加记录时日期
    # auto_add      每次更新记录,自动更新
    def __str__(self):
        return self.name

# 匹配日期，年月日，周，时分秒
# 匹配日期，date
User.objects.filter(create_time__date=datetime.date(2018, 8, 1))
User.objects.filter(create_time__date__gt=datetime.date(2018, 8, 2))
# 匹配年，year
User.objects.filter(create_time__year=2018)
User.objects.filter(create_time__year__gte=2018)
# 匹配日，day
User.objects.filter(create_time__day=8)
User.objects.filter(create_time__day__gte=8)
# 匹配周，week_day
User.objects.filter(create_time__week_day=2)
User.objects.filter(create_time__week_day__gte=2)


# 2.按天统计归档
"""
today = datetime.date.today()
select = {'day': connection.ops.date_trunc_sql('day', 'create_time')}
deploy_date_count = Task.objects.filter(
    create_time__range=(today - datetime.timedelta(days=7), today)
).extra(select=select).values('day').annotate(number=Count('id'))
Q 的使用
"""

# 3.update 不会自动更新 DateTimeField(auto_now_add=True,auto_now=True)
"""
使用save或update(status=2, update_time=datetime.now())
"""

# 4.django时区问题
# https://blog.csdn.net/ball4022/article/details/101670024
"""
不带时区的utc时间，称为naive time
带时区的utc时间，称为active time

"""