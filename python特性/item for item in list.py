# -*- coding:utf-8 -*-

list_a=[1,2,3,4,5]
list_b=[3,4,5,6,7]
old=[6,7,8,10]

#item for item in list_a if item not in list_b
it=[item for item in list_a if item not in list_b]
print(it)
print(item for item in list_a if item not in list_b)
new = [x ** 2 for x in old if not x % 2] #%取摸   not x%2是否为空
print(new)
print('abcd'*2)
print([item for item in old])