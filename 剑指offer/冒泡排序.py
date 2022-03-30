# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/27 21:53

a= []
for i in range(len-1):
    for j in range(len-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

