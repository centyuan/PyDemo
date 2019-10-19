#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-27 下午5:58
"""
描述
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

语法
index()方法语法：

list.index(x[, start[, end]])
参数
x-- 查找的对象。
start-- 可选，查找的起始位置。
end-- 可选，查找的结束位置。
返回值
该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
"""
aList = [123,'xyx','genie','notbe','unicorn']

print("genie索引位置:",aList.index('genie'))
