# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-30 下午3:32


print(dict.fromkeys(['a', 'b']))  # {'a': None, 'b': None}
# dict.copy() 函数返回一个字典的浅复制。
# 一:创建字典的不同方式
# 1.
a = dict(one=1, two=2, three=3)  # {'one': 1, 'two': 2, 'three': 3}
b = {'one': 1, 'two': 2, 'three': 3}  # {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # {'one': 1, 'two': 2, 'three': 3}
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'two': 2, 'one': 1})

# a=b=c=d=e

# 2.字典推导
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in dial_codes}
# {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}

# 二:字典合并四种方式 或 from collections import ChainMap
d1 = {'usr': 'root', 'pwd': '123456'}
d2 = {'ip': '127.0.0.1', 'port': '8080'}

# 1.dict.update方法
d3 = {}
d3.update(d1)
d3.update(d2)
print('dict.update:', d3)
# 2. python3.5后
d = {**d1, **d2}
print(d)

# 3.字典 dict(d1,**d2)
d3 = dict(d1, **d2)
print('dict():', d3)

# 4.字典的常规处理
for k, v in d1.items():
    d3[k] = v
for k, v in d2.items():
    d3[k] = v
print('四:', d3)

# 三:字典排序遍历

dict_data = {6: 9, 10: 5, 3: 11, 8: 2, 7: 6}
"""1、对字典按键（key）进行排序 （默认由小到大）"""

d0 = sorted(dict_data.keys())
print(d0)  # 输出结果[3, 6, 7, 8, 10]
d1 = sorted(dict_data.items(), key=lambda x: x[0])
print(d1)  # 输出结果[(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]

"""2、对字典按值（value）进行排序 （默认由小到大）"""
d2 = sorted(dict_data.items(), key=lambda x: x[1])
print(d2)  # 输出结果[('8', 2), ('10', 5), ('7', 6), ('6', 9), ('3', 11)]
d3 = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)
print(d3)  # 输出结果 [('3', 11), ('6', 9), ('7', 6), ('10', 5), ('8', 2)]
d4 = sorted(zip(dict_data.values(), dict_data.keys()))

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

"""3.dict_data.items()#以列表返回可遍历的(键, 值) 元组数组。"""
for key, value in dict.items():
    print(key, value)

"""4.enumerate 枚举"""
for i, v in enumerate(['tic', 'tac', 'toe']):
    print('枚举', i, v)

"""5.遍历两个或更多的序列，可以使用 zip() 组合"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q} It is {a}')
    # print('What is your {0}?  It is {1}.'.format(q, a))

"""6.sorted 函数的key= 参数没有调用str.uppper，而是把这个方法的引用传递给sorted 函数，这样在排序的时候，单词会被规范成统一格式"""
index = ["I", "love", "three", "things", "in", "the", "world", "The", "sun", "the", "moon"]
for word in sorted(index, key=str.upper):
    print(word)

# 7.排序(自定义排序) cmp_to_key
from functools import cmp_to_key

rank = [
    {'score': 12, 'time': '2022-08-04'},
    {'score': 23, 'time': '2022-08-01'},
    {'score': 23, 'time': '2022-07-24'},
    {'score': 10, 'time': '2022-07-16'},
]


def custom_sorted(x, y):
    # 先比较分数，分数相同在比较时间
    if x["score"] > y["score"]:
        return 1
    if x["score"] < y["score"]:
        return -1
    if x["score"] == y["score"]:
        if x["time"] > y["time"]:
            return -1
        else:
            return 1


to_rank = sorted(rank, key=cmp_to_key(custom_sorted), reverse=True)
# 类似的使用itemgetter排序
from operator import itemgetter

new_rank = sorted(rank, key=itemgetter('score'))  # 根据一个字段排序
new_rack = sorted(rank, key=itemgetter('score', 'time'))
new_rank = sorted(rank, key=lambda item:item['score'])
# 四:判断字典key是否存在

dict_data = {'name': 'yuan', 'age': 20, 'sex': 'man'}
# 1.python3 has_key()被__contains__(key)代替
print(dict_data.__contains__('name'))  # True

# 2.in
print('man' in dict_data)  # True
print('a' in dict_data)  # False

# 3. in keys
print('name' in dict_data.keys())  # True

# 五：获取最大最小值
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
# max(prices.values())
# 获取最大价格
# 只能得到key
print(max(prices, key=lambda k: prices[k]))  # HPQ 输出键
# zip后，key,value都有
print(max(zip(prices.values(), prices.keys())))  #

# 六:删除字典value为空的键值对

test_dict = {
    'id': 1,
    'name': 'name',
    'age': 18,
    'sex': 'man',
    '空': '',
    'o': 0,
    'bool': False,
    'None': None,
    'new_None': 'None'
}
# for key in test_dict.keys():
#     if not test_dict.get(key):
#         del test_dict[key]
# 字典生成器
new_data = {k: v for k, v in test_dict.items() if v}
# if v 去掉所有‘空值'
# {'id': 1, 'name': 'name', 'age': 18, 'sex': 'man', 'new_None': 'None'}
new_data = {k: v for k, v in test_dict.items() if v is not None}
# if is not None 去掉None
# {'id': 1, 'name': 'name', 'age': 18, 'sex': 'man', '空': '', 'o': 0, 'bool': False, 'new_None': 'None'}

