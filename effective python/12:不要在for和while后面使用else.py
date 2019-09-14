#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午8:22

"""
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
while … else 也是一样。

try ....except...else 语句，当没有异常发生时，else中的语句将会被执行
try ...finally 无论异常是否发生，在程序结束前，finally中的语句都会被执行。

"""
#1.for 在循环正常执行完，会立即执行else,break则不执行else


#2.for 循环的序列为空，那么会立即执行else
#  whiel False: 如果后面跟着else,那它会立刻执行

