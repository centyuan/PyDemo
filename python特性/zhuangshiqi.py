# -*- coding:utf-8 -*-
"""
＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西（取决于装饰器的返回值），
1如果装饰器函数的返回值为普通变量，那么被修饰的函数名就变成了变量名；
2如果装饰器返回的是一个函数的名称，那么被修饰的函数名依然表示一个函数
"""
#1:funA 作为装饰器函数
def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"
@funA
def funB():
    print("学习 Python")
#2:带参数的函数装饰器
#嵌套一个函数，该函数带有的参数个数和被装饰器修饰的函数相同
def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:",arc)
    return say
@funA
def funB(arc):
    print("funB():",'a')
funB("http://c.biancheng.net/python")
#2等价于
def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:", arc)

    return say


def funB(arc):
    print("funB():", 'a')


funB = funA(funB)
funB("http://c.biancheng.net/python")

#3:多个参数 ，*args 和 **kwargs 表示接受任意数量和类型的参数。
def funA(fn):
    # 定义一个嵌套函数
    def say(*args,**kwargs):
        fn(*args,**kwargs)
    return say
@funA
def funB(arc):
    print("C语言中文网：",arc)
@funA
def other_funB(name,arc):
    print(name,arc)
funB("http://c.biancheng.net")
other_funB("Python教程：","http://c.biancheng.net/python")

if __name__ == '__main__':
    print(funB)

