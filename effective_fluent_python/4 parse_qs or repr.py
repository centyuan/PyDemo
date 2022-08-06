#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-12 下午11:06

from urllib import parse
"""
url字符编码
编码的格式为：%加字符的ASCII码，即一个百分号%，后面跟对应字符的ASCII（16进制）码值
例如 空格的编码值是"%20"。
"""
# 1.parse_qs将 url编码字符串 转成 字典

test_str = 'red=1&blue=3&green=5'
my_value = parse.parse_qs(test_str,keep_blank_values=True)
print(my_value) #{'red': ['1'], 'blue': ['3'], 'green': ['5']}
#2将字典转成 url编码字符串
new_value = parse.urlencode(my_value)
print(new_value)

#---before 5
