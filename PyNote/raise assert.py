# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan


"""
手动抛出异常
raise [exceptionName [(reason)]]
"""

# 一:异常处理
"""
调用栈
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，
就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
"""
try:
    print("try...")
    r = 10 / int("a")
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:  # 可以有多个except来捕获不同类型的异常
    print("ZeroDivisionError:", e)
else:  # 没有错误发生
    print("no error!")
finally:  # 都会执行
    print("finally...")
print("END")

# 二:自定义抛出错误 raise
"""
因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，
而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
一旦执行了raise语句,raise之后的语句不在执行
如果加入了try,except,那么except里的语句会被执行

raise和raise..from区别:
在显示错误信息时，raise只显示错误类型，raise...from...还会显示导致错误的原因（原因是from 后面的部分）
"""

from typing import Any, List


class FooError(ValueError):
    def __init__(self, error: str, *args: List[Any]):
        super().__init__(*args)
        self.error = error

    def __str__(self):
        return self.error


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)  # 自定义异常
        raise ValueError("invalid value: %s" % s)
    return 10 / n


# foo('0')


def bar():
    try:
        foo("0")
    except ValueError as e:
        print("ValueError!")
        raise ValueError("错误") from e  # 只有一个raise


# bar()

# 三:assert
"""
python assert断言检查某个条件表达式是否为真,其返回值为假，就会触发异常。
可以理解assert断言语句为raise-if-not，
"""
print("assert:")
a = 888
assert type(a) == str, "a is type of int"  # 后面为异常信息

# result：
# Traceback (most recent call last):
#   File "F:/gitHub/OrmCommand/app/new_main.py", line 20, in <module>
#     assert type(a) == str,'a is type of int'
# AssertionError: a is type of int
