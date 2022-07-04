# -*- coding:utf-8 -*-
import time
import calendar

print('time.time():',time.time())  # 时间戳--1970年是距今最早的的1月1日是星期一的日期
print('time.localtime():',time.localtime())
time_classS=time.localtime()
print(type(time_classS),time_classS.tm_year)
print('time.asctime()：',time.asctime())

print('时间元组：',time.localtime(time.time()))#时间元组
print('可读的格式化时间：',time.asctime(time.localtime(time.time())))#可读的格式化时间
#格式化日期
#我们可以使用 time 模块的 strftime 方法来格式化日期，：
#time.strftime(format[, t])
print('time.strftime--%Y-%m-%d %H:%M:%S:',time.strftime("%Y-%m-%d %H:%M:%S"))
print('time.strftime--%a %b %d %H:%M:%S %Y:',time.strftime("%a %b %d %H:%M:%S %Y"))
#print(time.strftime('%Y-%m-%d %H：%M：%S'))
print("以下输出2016年1月份的日历:")
print(calendar.month(2018, 2))

import datetime
# date  处理年月日
# time  处理时分秒
# datetime  date和time综合利用
# timedelta  做时间加减
# tzinfo    时区类
print("当前时间和日期",datetime.datetime.now())  # 2022-05-17 21:23:56.150028 类型为datetime对象类型
print('定时时间',datetime.date(2017,3,22))
print('前一天时间',datetime.datetime.now()-datetime.timedelta(days=1,hours=1,minutes=30))
print(datetime.timedelta(hours=1,minutes=40))