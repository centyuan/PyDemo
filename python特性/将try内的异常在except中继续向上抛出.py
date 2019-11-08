#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-11 下午8:56

"""
raise 本身就是抛出异常的作用（含义）。

所以当我们想要在 except 内部抛出另外一个异常，就使用 raise <SomeError>

但是如果我们想要将原本来自 try 内部的异常，在 except 中继续（往上）抛出的话，要嘛直接使用 raise，即：


"""
#1
# try:
#     raise IndexError('in try')
# except IndexError as err:
#     print(' 1 except')
#     raise

"""
又或者我们想要对这个异常换一种异常类（换一种表示异常含义，比如自己定义的异常类等），
那么就应当使用 raise ... from <last_error_instance>， 即：
"""
# 2 可以对这个异常换一种表示异常的含义，比如自己定义的异常类
"""
raise 与raise..from的区别主要在于：
在显示错误信息时，raise只显示错误类型，raise...from...还会显示导致错误的原因（原因是from 后面的部分）
"""

try:
    raise IndexError("in try")
except IndexError as err:
    print('2 except')
    raise ValueError('invalid inputs ') from err
    # raise ValueError('invalid inputs')

