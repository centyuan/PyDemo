# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 15:47

import operator

action = {
    "+":operator.add,
    "-":operator.sub,
    "/":operator.truediv,
    "*":operator.mul,
    "**":pow
}
print(action['-'](50,25))