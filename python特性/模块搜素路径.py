# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-22 下午12:47
"""
sys.paht:模块搜索路径
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
首先判断这个module是不是built-in即内建模块，如果是则引入内建模块，
不是则搜索sys.path中的路径列表(
1.当前目录
2.如果不在当前目录，Python则搜索变量PYTHONPATH后面的每个目录。
如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

通常__init__.py 文件为空：但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的__init__.py文件。

"""
import sys
import os

print(sys.path)
"""
step1.为待导入的模块创建module类的实例：模块对象(目前是空对象)将该module对象 插入sys.modules中
step2：将该module对象 插入sys.modules中；
step3：装载module的代码（如果需要，需先编译）；
step4：执行新的module中对应的代码。
"""
# 1.控制模块被全部导入的内容
__all__ = []  # 控制导出

# 2. 相对路径导入包中子模块
# from . import args_kwargs
# from ..B import bar

# 3.添加路径以便import
sys.path.append('path')
# sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__))),'src')



