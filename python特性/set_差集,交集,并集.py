# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

t = [1, 2, 3, 4]
s = [3, 4, 5, 6]

a = list(set(t) | set(s))  # 并集

b = list(set(t) & set(s))  # 交集

c = list(set(t) - set(s))  # 差集

d = list(set(t) ^ set(s))  # 对称差集
abcd = ["B", "A", "C"]
efgh = ["A", "B", "C"]
yi = ["A"]
er = ["A", "C"]

cccc = list(set(yi) - set(er)) or list(set(er) - set(yi))  # 返回有值的
print('ccc',list(set(yi)-set(er)),list(set(er)-set(yi)))

ss = list(set(abcd) - set(efgh))
if not ss:
    print(ss)


