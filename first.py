# -*- coding:utf-8 -*-

print('helloword'[2])
print(type({1,2,3}))
print(4/2)
a={'1':'nhao','2':'ssss'}
b={'1':'nhao','2':'ssss'}
d=a
c={'2':'nhao','1':'ssss'}#可变类型
e='23' #不可变类型
f='23'
g=e
print(a==b)
print(a==c)
print(a is b )
print(a is d)
print(id(a))
print(id(b))
print(id(d))
print(id(e))
print(id(f))
print(id(g))

