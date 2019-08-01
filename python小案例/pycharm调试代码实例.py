#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-22 下午4:09

#以下三种调试方式
#一:pycharm debug
#二:python pdb
#三:python ipdb

"""
使用 ipdb 调试 Python
1、安装

　　pip install ipdb

2、使用

　　python -m ipdb xxx.py

　　程序内部：

　　from ipdb import set_trace

      set_trace()

3、常用命令

ENTER(重复上次命令)
c(继续)
l(查找当前位于哪里)
s(进入子程序)
r(运行直到子程序结束)
!<python 命令>
h(帮助)
a(rgs) 打印当前函数的参数
j(ump) 让程序跳转到指定的行数
l(ist) 可以列出当前将要运行的代码块
n(ext) 让程序运行下一行，如果当前语句有一个函数调用，用 n 是不会进入被调用的函数体中的
p(rint) 最有用的命令之一，打印某个变量
q(uit) 退出调试
r(eturn) 继续执行，直到函数体返回
s(tep) 跟 n 相似，但是如果当前有一个函数调用，那么 s 会进入被调用的函数体中


"""