#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-27 下午5:24
"""
语法
replace()方法语法：

str.replace(old, new[, max])
参数
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
"""
str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))
print(str.replace("is", "was", 3))