# -*- coding:utf-8 -*-
a = {'a': '0', 'b': '1', 'c': '2', 'd': '3'}
t = a.keys()
b = 'a'
print({k: v for k, v in a.items() if b in t})  # 输出1

temp = {}
for k, v in a.items():
    if b in t:
        temp[k] = v
print(temp)
 # 输出2
