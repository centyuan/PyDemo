# -*- coding:utf-8 -*-
import time
import calendar
import datetime
# 1.时间time
t = time.time()
print('time.time():', time.time())
print(t)  # 原始时间数据--1970年是距今最早的的1月1日是星期一的日期
print(int(t))  # 秒级时间戳
print(int(round(t * 1000)))  # 毫秒级时间戳
print(int(round(t * 1000000)))  # 微秒级时间戳
print('time.localtime():', time.localtime())
time_classS = time.localtime()
print(type(time_classS), time_classS.tm_year)
print('time.asctime()：', time.asctime())

# 时间元组
print('时间元组：', time.localtime(time.time()))
# 可读的格式化时间
print('可读的格式化时间：', time.asctime(time.localtime(time.time())))
# 使用 time 模块的 strftime 方法来格式化日期：time.strftime(format[, t])
print('time.strftime--%Y-%m-%d %H:%M:%S:', time.strftime("%Y-%m-%d %H:%M:%S"))
print('time.strftime--%a %b %d %H:%M:%S %Y:', time.strftime("%a %b %d %H:%M:%S %Y"))
# 字符串转为日期
text = '2022-09-20'
print('字符串转为日期：',datetime.datetime.strptime(text,"%Y-%m-%d"))   # 性能很差
print("以下输出2016年1月份的日历:")
print(calendar.month(2018, 2))

# 2.日期datetime


# date  处理年月日
# time  处理时分秒
# datetime  date和time综合利用
# timedelta  做时间加减
# tzinfo    时区类
print("当前时间和日期:", datetime.datetime.now())  # 2022-05-17 21:23:56.150028 类型为datetime对象类型
print('指定时间:', datetime.date(2017, 3, 22))
print('指定日期时间', datetime.datetime(2017, 3, 22)) # 比datetime.datetime.strptime() 快7倍多
print('前一天时间', datetime.datetime.now() - datetime.timedelta(days=1, hours=1, minutes=30))
print('时间段', datetime.timedelta(hours=1, minutes=40) + datetime.timedelta(hours=2, minutes=20))
print('转为时间戳', datetime.datetime.now().timestamp())


