#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午9:46

"""
在python3中的zip函数,可以把两个或两个以上的迭代器封装为生成器
"""
names = ['Cecilia','Lise','Marie']
letters = [len(n) for n in names]

#1.原始写法
longest_name = None
max_letters = 0
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

#2.使用enumerate
longest_name = None
max_letters = 0
for i,name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

#3.使用zip
longest_name = None
max_letters = 0
for name,count in zip(names,letters):
    if count >max_letters:
        longest_name = names
        max_letters = count
print(longest_name)
