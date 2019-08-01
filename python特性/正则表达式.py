# -*- coding:utf-8 -*-
import re
"""
1、. 匹配任意除换行符“\n”外的字符；
2、*表示匹配前一个字符0次或无限次；
3、+或*后跟？表示非贪婪匹配，即尽可能少的匹配，如*？重复任意次，但尽可能少重复；
4、 .*? 表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
如：a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。

"""
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#re.search 扫描整个字符串并返回第一个成功的匹配
#re.findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#pattern = re.compile(r'\d+')
#m = pattern.match('one12twothree34four')
#re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
a='C|C++|Java|c#|Python|Javascript'
b='py1aaa2thona123333ja1sss2va43241ccc2++'
c='python 11java  javascript'
d="""centyuan
   """
s="ip='230.192.168.78',version='1.0.0',ip='230.192.168.20',version='1.0.0'，ip='230.192.168.100',version='1.0.0'"
result=re.findall("ip='(?P<ip>\d+.\d+.\d+.\d+)",s) ##正则表达式分组(?P<name>)分组命名
result1=re.findall("(?P<ip>\d+.\d+.\d+.\d+)",s)
print("result1",result1)
print(result[1])
print(re.search("ip='(?P<ip>\d+.\d+.\d+.\d+)",s).group('ip'))
a1=re.findall('Python',a)
print(a1)
b1=re.findall('1[a-z]*2',b)
b2=re.findall('1([a-z]*)2',b)
print(re.findall('c(\d+)',b))#正则表达式分组的概念
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