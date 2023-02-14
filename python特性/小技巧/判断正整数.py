# _*_ coding:utf-8 _*_
# @Author : centyuan

# ceil返回数字的上入整数:1.3返回2
# int 返回数字的下入整数:1.1放回1
value = input('输入:')

if type(value) == type(int(value)) and value > 0:
    print(True)
