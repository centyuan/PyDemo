#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午5:23
#split() 方法语法：
#
# str.split(str="", num=string.count(str)).
# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有
#返回值
#返回分割后的字符串列表。
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str.split( ))       # 以空格为分隔符，包含 \n
print(str.split(' ', 1 )) # 以空格为分隔符，分隔成两个

#['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
#['Line1-abcdef', '\nLine2-abc \nLine4-abcd']