# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:32

#1
a ={'x':1,'y':2}
b ={'y':3,'z':4}
c = a.copy()
c.update(b)
print(a,b,c)

#2 python3.5后

d = {**a,**b}
print(d)

#两个列表转发为字典
keys =[1,2,3]
values = ['a','b','c']
print(dict(zip(keys,values)))