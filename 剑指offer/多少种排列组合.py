# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 16:05

"""
range(1,4) 数字123能组成多少个互不相同且无重复的三位数
"""
res = 0
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and i != k and j != k:
                res += 1
print(res)
#1、2、3、4、5 能组成多少个互不相同且无重复的三位数
i = 0
for x in range(1, 6):
    for y in range(1, 6):
        for z in range(1, 6):
            if (x != y) and (y != z) and (z != x):
                i += 1
                if i % 4:
                    print("%d%d%d" % (x, y, z), end=" | ")
                else:
                    print("%d%d%d" % (x, y, z))
print(i)