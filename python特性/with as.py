# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-27 上午11:10

# With语句是什么？
# 有一些任务，可能事先需要设置，事后做清理工作。
# 对于这种场景，Python的with语句提供了一种非常方便的处理方式。
# 一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。

# 1:不用with语句，代码如下：

file = open('/home/ssr.json')
data = file.read()
file.close()
# 这里有两个问题。
# 一是可能忘记关闭文件句柄；
# 二是文件读取数据发生异常，没有进行任何处理。
# 下面是处理异常的加强版本：
file = open("/home/ssr.json")
try:
    data = file.read()
finally:
    file.close()

# 虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了
# 除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。
# 下面是with版本的代码：
with open('home/ssr.json') as file:
    data = file.read()
