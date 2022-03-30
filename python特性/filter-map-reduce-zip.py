#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 下午4:23

#filter函数是一个筛选函数
#filter将传入的函数依次作用到序列的每个元素，True则返回 False则不返回。
list2=[1,2,3,4,5,6,7,8,9]
def a(x):
    return x%2==1
print(filter(a,list2))#返回值类型是filter对象 生成器对象
print(list(filter(a,list2)))
print(list(filter(lambda a:a%2==1,list2)))
#map 函数是一个计算函数 参数（函数，可迭代对象）
#  会将可迭代对象的值经过函数计算后返回
my_map=map(lambda x:x+1,range(10))
print(my_map) # 返回值类型是map对象 生成器对象
print(list(my_map))

#reduce 函数也是一个计算函数 参数（函数，可迭代对象）
#   会将可迭代对象的值依次在函数中累计运算 Python3中需要导入
from functools import reduce
my_reduce=reduce(lambda x,y:x+y,range(10)) #[0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_reduce)# 返回 计算后结果 45

#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
a = [1,2,3]
b = [2,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
print(zipped,type(zipped))
for i in zipped:
    print(i)
zip(a,c) #元素个数与最短的列表一致
a1,b1= zip(*zip(a,c)) #与zip相反，理解为解压

print(a1,b1)

print(bool)
