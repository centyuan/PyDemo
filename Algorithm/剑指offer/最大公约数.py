# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 16:12
def f(a, b):
    if b == 0:
        return a
    else:
        return f(b, a % b)


#a, b = input("Enter two natural numbers: ")
a,b = 20 ,4
print(f(a, b))
a,*b,c=range(5)
print(a,b,c)