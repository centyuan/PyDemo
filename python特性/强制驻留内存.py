# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 13:33
"""
int
Python 将一个 -5~256 之间整数列表预加载（缓存）到内存中，
我们在这个范围内创建一个整数对象时，python会自动引用缓存的对象，不会创建新的整数对象。
string
小于20会自动驻留
"""

# 强行驻留
import sys

letter_d = 'd'

a = sys.intern('hello world')
# b = sys.intern('hello worl' + 'd')
# c = sys.intern(' '.join(['hello', 'world']))
a1 = 'hello world'
# 只要是hello world都一样
print('a:', a, id(a))  # hello world 1906900377008
# print('b:', b, id(b))  # hello world 1906900377008
# print('c:', c, id(c))  # hello world 1906900377008
print('a1:', a1, id(a1))  # hello world 1906900377008

d = 'hell yuan'
e = 'hell yua' + 'n'
f = ' '.join(['hell', 'yuan'])
print('d:', d, id(d))  # hell yuan 2814434801264
print('e:', e, id(e))  # hell yuan 2814434801264
print('f:', f, id(f))  # hell yuan 2814434802096
