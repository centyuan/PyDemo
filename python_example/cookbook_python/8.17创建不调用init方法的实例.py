"""
通过__new__()创建一个未初始化的实例
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.monty = month
        self.day = day


d = Date.__new__(Date)
data = {'yeadr': 2022, 'month': 9, 'day': 26}
for key, value in data.items():
    # 初始化
    setattr(d, key, value)
