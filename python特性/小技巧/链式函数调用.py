# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:26

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

a,b=4,5
print((subtract if a>b else add)(a,b))

