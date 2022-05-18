# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 20:55
import os

with open('./Cap') as today:
    count= 0
    for i in today.read():
        print("---",i)
        if i.isupper():
            count +=1
    print(count)



