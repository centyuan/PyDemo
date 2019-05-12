# -*- coding:utf-8 -*-
import  time
import calendar

print('time.time():',time.time())#时间戳
print('time.localtime():',time.localtime())
print('time.asctime()',time.asctime())

print(time.localtime(time.time()))#时间元组
print(time.asctime(time.localtime(time.time())))#可读的格式化时间
#格式化日期
#我们可以使用 time 模块的 strftime 方法来格式化日期，：
#time.strftime(format[, t])
print('time.strftime--%Y-%m-%d %H:%M:%S:',time.strftime("%Y-%m-%d %H:%M:%S"))
print ('time.strftime--%a %b %d %H:%M:%S %Y:',time.strftime("%a %b %d %H:%M:%S %Y"))

print(time.strftime('%Y-%m-%d %H：%M：%S'))

print ("以下输出2016年1月份的日历:")
print (calendar.month(2018, 2))
print(time.strftime("%Y-%m-%d %H:%M:%S"))