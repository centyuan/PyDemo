import time
import calendar
# datetime是对time模块的封装
import datetime
from wsgiref.handlers import format_date_time

# 1.时间time
t = time.time()
print('时间戳time.time():', t)  # 原始时间数据--1970年是距今最早的的1月1日是星期一的日期
print('秒级时间戳:', int(t))
print('毫秒级时间戳:', int(round(t * 1000)))
print('微秒级时间戳:', int(round(t * 1000000)))

# 2.时间元组即struct_time对象
struct_time = time.localtime()
print('时间元组:', struct_time, struct_time.tm_year, struct_time.tm_mday,struct_time.tm_hour)
print('转为时间元组:', time.localtime(time.time()), time.localtime(1670848011))
print('时间元组转为时间戳:', time.mktime(time.localtime()))

# 3.可读的格式化时间
print('可读的格式化时间time.asctime():', time.asctime())
print('时间元组转可读的格式化时间:', time.asctime(time.localtime(time.time())))
print('输出当前时间,time.strftime--%Y-%m-%d %H:%M:%S:', time.strftime("%Y-%m-%d %H:%M:%S"))
print('输出当前时间,time.strftime--%a %b %d %H:%M:%S %Y:', time.strftime("%a %b %d %H:%M:%S %Y"))
print('显示指定格式时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 4.字符串转为日期
# print('字符串转为日期：', datetime.datetime.strptime('2022-09-20', "%Y-%m-%d"))  # 性能很差
print('字符串转为日期：', time.strptime('2022-09-20', "%Y-%m-%d"))  # 性能很差
print("以下输出2016年1月份的日历:")
print(calendar.month(2018, 2))

# 5.datetime模块
# date  处理年月日
# time  处理时分秒
# datetime  date和time综合利用
# timedelta  做时间加减
# tzinfo    时区类
date_object = datetime.date.today()
print("当前日期:", datetime.date.today(), datetime.date.today().year, datetime.date.today().month,)
print('指定时间:', datetime.date(2017, 3, 22), datetime.date.fromtimestamp(1670848796))
print('修改时间,日期改为1号:', datetime.date.today().replace(day=1))
print('返回weekday', date_object.weekday(), date_object.isoweekday(), date_object.isoformat())
print("当前时间:", datetime.datetime.now())  # 2022-05-17 21:23:56.150028 类型为datetime对象类型
print('指定日期时间:', datetime.datetime(2017, 3, 22))  # 比datetime.datetime.strptime() 快7倍多
print('前一天时间:', datetime.datetime.now() - datetime.timedelta(days=1, hours=1, minutes=30))
print('时间段:', datetime.timedelta(hours=1, minutes=40) + datetime.timedelta(hours=2, minutes=20))
print('转为时间戳:', datetime.datetime.now().timestamp())
print('转为时间元组timetuple:', datetime.datetime.now().timetuple())
print('某月天数:', calendar.monthrange(2022, 11), (datetime.date(2022, 10, 1) - datetime.date(2022, 9, 1)).days)

# 6.计算时间差
from dateutil import rrule

date1 = "2022-10-08"
date2 = "2022-10-10"
date_1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
date_2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
print('时间差', (date_2 - date_1).days)
print('时间差', (date_2 - date_1).seconds)
weeks = rrule.rrule(rrule.WEEKLY, dtstart=date_1, until=date_2).count()  # 周数差
months = rrule.rrule(rrule.MONTHLY, dtstart=date_1, until=date_2).count()  # 月数差
years = rrule.rrule(rrule.YEARLY, dtstart=date_1, until=date_2).count()  # 年数差
# days = rrule.rrule(rrule.DAILY, dtstart=date1, until=date2).count()  # 天数差

# 7.000Z and RFC1123日期格式
print('000Z:', datetime.datetime.strptime("2022-10-11T02:31:23.000Z", "%Y-%m-%dT%H:%M:%S.000Z"))
print('RFC1123日期格式:', format_date_time(time.mktime(datetime.datetime.now().timetuple())))
