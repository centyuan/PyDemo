#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-12 上午11:31
#如何生成斐波那契數列
def fab(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1

fab(5)

def fab1(max):
    n,a,b=0,0,1
    l=[]
    while n<max:
        l.append(b)
        a,b=b,a+b
        n=n+1
    return l
for n in fab1(4):
    print(n)