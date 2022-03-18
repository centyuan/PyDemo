#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-21 下午2:57

"""

raise 手动抛出异常
系统是否要引发异常，可能需要根据应用的业务需求来决定
(如果程序中的数据、执行与既定的业务需求不符，这就是一种异常。
由于与业务需求不符而产生的异常，必须由程序员来决定引发，系统无法引发这种异常)
该语句的基本语法格式为：

raise [exceptionName [(reason)]]
"""


#一:异常处理
"""
调用栈
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，
就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
"""
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e: #可以有多个except来捕获不同类型的异常
    print('ZeroDivisionError:', e)
else:   # 没有错误发生
    print('no error!')
finally:  #都会执行
    print('finally...')
print('END')

#二:自定义抛出错误 raise
"""
因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，
而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
一旦执行了raise语句,raise之后的语句不在执行
如果加入了try,except,那么except里的语句会被执行
"""
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')




def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()


#三:assert
"""
python assert断言检查某个条件表达式是否为真,其返回值为假，就会触发异常。
可以理解assert断言语句为raise-if-not，

在表达式expression1为假的时候，结束程序，抛出断言类错误（AssertionError: expresssion2）,
表达式expression2可有可无。*当然，如果expression为真的时候，什么都不做，继续往下执行。


"""
a = 888
assert type(a) == str,'a is type of int'

# result：
# Traceback (most recent call last):
#   File "F:/gitHub/OrmCommand/app/test.py", line 20, in <module>
#     assert type(a) == str,'a is type of int'
# AssertionError: a is type of int

