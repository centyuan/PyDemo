#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午8:48

#一:通常不会判断result是否为None,不能很好定位错误
def divide(a,b):
    try:
        return  a/b
    except ZeroDivisionError:
        return  None

result = divide(10,5)
if result is None:
    print("Invalid input")

#二：改进1
def divide(a,b):
    try:
        return  True,a/b
    except ZeroDivisionError:
        return  False,None

success,result = divide(6,3)
print(success,result)
_,result = divide(10,2) #习惯使用(_,result)这种写法来表示用不到的变量
print(result)

#三：改进2
def divide(a,b):
    try:
        return  a/b
    except ZeroDivisionError as e:
        raise  ValueError('Invalid inputs') from e

#next 15
