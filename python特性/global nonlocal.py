# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/29 14:59

"""
1:global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，
而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，
nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。

2:global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，
global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，并且外层函数中定义了相应的局部变量，否则会发生错误

"""
def func():
    x = 'hello func'
    print('func', x, id(x))

x = 'hello main'
print('main1', x, id(x))
func()
print('main2', x, id(x))
'''
 在函数内部使用了与全局变量同名的变量，如果不对该变量赋值（修改变量），
 那么该变量就是全局变量，如果对该变量进行赋值(重新创建一个该变量对象)，那么该变量就是局部变量。
'''
def func():
    global x
    x = 'hello func'

"""
如果在嵌套函数和函数（这里指包含嵌套函数的那个函数）中存在和全局变量同名的变量，
如果直接使用，而不修改变量的值，那么这三个位置的变量使用的是同一个全局变量，
如果在函数中修改了变量值，那么该变量会被标识为该函数的局部变量，
嵌套函数直接使用时使用的是该函数的局部变量。如果在嵌套函数中修改同名变量的值，
那么嵌套函数中的该变量会被标识为该嵌套函数的局部变量，它的修改不影响函数中同名变量和全局变量。
"""
# https://blog.csdn.net/xcyansun/article/details/79672634
def func():
    x = "hello func"
    print("func1", x, id(x))
    def ifunc():
        #nonlocal x
        x = "hello ifunc"
        print("ifunc", x, id(x))
    ifunc()
    print("func2", x, id(x))
x = "hello main"
print("main1", x, id(x))
func()
print("main2", x, id(x))
"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
"""