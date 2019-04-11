#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 上午11:20
#一：
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(id(l))
    print(l)


f(2)  # [0,1]
f(3, [3, 2, 1])  # [3,2,1,0,1,4]
f(3)  # [0,1,0,1,4]
f(3)
f(3)

#二：

class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)  # 1 1 1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)  # 1 2 1
Child2.x = 3
print(Parent.x, Child1.x, Child2.x)  # 1 2 3

#三：
def mul():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in mul()])  # 6 6 6 6

#四：列表去重
list1=[9,4,2,5,8,4,5,3]
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)

new_list={}.fromkeys(list1).keys()
print(new_list)
