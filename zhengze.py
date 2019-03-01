# -*- coding:utf-8 -*-
import re
a='C|C++|Java|c#|Python|Javascript'
b='py1aaa2thon123333ja1sss2va43241ccc2++'
c='python 11java  javascript'
a1=re.findall('Python',a)
print(a1)
b1=re.findall('1[a-z]*2',b)
b2=re.findall('1([a-z]*)2',b)
print(b1)
print(b2)
c1=re.findall('[a-z]{3,6}',c)#默认是贪婪的 '[a-z]{3,6}?'非贪婪
print(c1)

language='PythonC#JavaC#PHPC#'
def convert(value):
    mat=value.group()
    return '!!'+mat+'!!'
r=re.sub('C#',convert,language)
print(r)

#例1
def f1():
    a=10
    def f2():
        a=20
        print(a)
    print(a)
    f2()
    print(a)
f1()
#例二
#def ff1():
#    a=10
#    def ff2():
#        c=20+a #等号左边会被认为局部变量
#    return ff2()
#f=ff1()
#print(f)
#print(f.__closure__)
#匿名函数
add = lambda x, y : x+y
add(1,2)  # 结果为3
#三元表达式
x1=2
y1=3
#python没有这种方式t= x1 >y1 ? x1:y1
r=x1 if x1>y1 else y1
list_X=[1,2,3,4,5,6,7,8]
ruslts=map(lambda x:x*x,list_X)#map reduce filter
print(ruslts)