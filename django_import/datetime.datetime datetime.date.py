# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/28 10:40
from datetime import datetime
print(datetime.now())  # 2019-10-28 10:41:27.201551
import datetime
print(datetime.date(2019,10,28)) # 2019-10-28


from django.db import models
from datetime import datetime
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    add_time = models.CharField(default=datetime.now)
    date = models.DateField(auto_now_add=True)
    # auto_now_add  自动添加,以添加记录时日期
    # auto_add      每次更新记录,自动更新
    def __str__(self):
        return self.name

# 匹配日期，date
User.objects.filter(create_time__date=datetime.date(2018, 8, 1))
User.objects.filter(create_time__date__gt=datetime.date(2018, 8, 2))

# 匹配年，year
User.objects.filter(create_time__year=2018)
User.objects.filter(create_time__year__gte=2018)

# 匹配月，month
User.objects.filter(create_time__month__gt=7)
User.objects.filter(create_time__month__gte=7)

# 匹配日，day
User.objects.filter(create_time__day=8)
User.objects.filter(create_time__day__gte=8)

# 匹配周，week_day
User.objects.filter(create_time__week_day=2)
User.objects.filter(create_time__week_day__gte=2)

# 匹配时，hour
User.objects.filter(create_time__hour=9)
User.objects.filter(create_time__hour__gte=9)

# 匹配分，minute
User.objects.filter(create_time__minute=15)
User.objects.filter(create_time__minute_gt=15)

# 匹配秒，second
User.objects.filter(create_time__second=15)
User.objects.filter(create_time__second__gte=15)


# 按天统计归档
# today = datetime.date.today()
# select = {'day': connection.ops.date_trunc_sql('day', 'create_time')}
# deploy_date_count = Task.objects.filter(
#     create_time__range=(today - datetime.timedelta(days=7), today)
# ).extra(select=select).values('day').annotate(number=Count('id'))
# Q 的使用