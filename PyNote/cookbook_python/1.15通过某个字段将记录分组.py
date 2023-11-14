"""
有一个字典或实例的序列,根据特定字段如date分组
"""
rows = [
    {'address': '成都', 'date': '2022-07-22'},
    {'address': '自贡', 'date': '2022-08-12'},
    {'address': '乐山', 'date': '2022-08-10'},
    {'address': '杭州', 'date': '2022-07-22'},
    {'address': '深圳', 'date': '2022-07-22'},
    {'address': '上海', 'date': '2022-08-10'},
    {'address': '重庆', 'date': '2022-08-12'},
    {'address': '武汉', 'date': '2022-08-10'},
]
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

# 先排序
rows.sort(key=itemgetter('date'))  # 排序
rows_by_date = defaultdict(list)   # list多值字典
for date, items in groupby(rows, key=itemgetter('date')):
    # groupby仅仅检测连续的元素，所以先排序
    print(date, items)  # items为groupby返回的迭代器
    # rows_by_date[date].extend(list(items))
    for i in items:
        print('迭代器', i)
print(rows_by_date)
print(rows_by_date['2022-07-22'])


