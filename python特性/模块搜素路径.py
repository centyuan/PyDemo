#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-22 下午12:47
"""
搜索路径
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

"""
import  sys

print(sys.path)