#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-23 下午5:17

from django_import.utils.timezone import now,datetime,timedelta

"""
.strftime 将<date,datetime,timezone.now()等类型处理转化为字符串类型
.strptime 将字符串类型处理转化成期望(datetime)类型的数据
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）  十二小时制
%M 分钟数（00=59）
%S 秒（00-59）　
.replace()
"""
#一:
abc = now()
cba = abc.strftime("%Y-%m-%d<>%H:%M:%S")
print(abc,cba)

#二:
d2 = datetime.strptime('2018-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')

#三:
start_time = now()
end_time = start_time + timedelta(days=30,hours=1)
