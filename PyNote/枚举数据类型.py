"""
枚举:指列出有穷集合中的所有元素,在python中可以视为一种数据类型

"""


# 1.通过类实现:两个问题(1枚举项可以重复,2值可以被外部修改)
class Weekday():
    monday = 1
    tuesday = 2
    wednesday = 3
    thirsday = 4
    friday = 5
    saturday = 6
    sunday = 7
    wednesday = 333


print(Weekday.friday)
print(Weekday.wednesday)  # 333
Weekday.friday = "星期五"

# 2.通过enum模块实现,
from enum import Enum


class Weekday2(Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thirsday = 4
    friday = 5
    saturday = 6


print(Weekday2.wednesday)
print(Weekday2.wednesday.name)  # 获取变量名称
print(Weekday2.wednesday.value)  # 获取变量值
