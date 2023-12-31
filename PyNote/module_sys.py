# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

import sys
import os

# sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分。
# 1.sys.path

"""
import的搜索顺序:
首先判断这个module是不是built-in即内建模块，如果是则引入内建模块，如果不是则在一个称为sys.path的list中寻找
sys.path在python脚本执行时动态生成，包括以下3个部分：
1、脚本执行的位置，即当前路径
2、环境变量中的PYTHONPATH, 即.bash_profilec.
3、安装python时的依赖位置

"""
###   python搜索模块的顺序为:内建模块>当前路径，即执行Python脚本文件所在的路径>环境变量中的PYTHONPATH>python安装路径
print(sys.path)  # sys.path.append("")备注:这个添加只是临时添加，如果退出当前会话，或者当前的shell，就会消失。
sys.path.append('引用模块的地址')
sys.path.insert(0, '引用模块的地址')  # 优先与其他被important检查
print(sys.path)
print("PATH", os.environ['PATH'])  # os.environ["PATH"] += "新系统环境值"，
print("PYTHONPATH", os.environ['PYTHONPATH'])

# 2. sys.argv
"""
sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键，
所以那些试图从代码来说明它作用的解释一直没看明白。因为我们从外部取得的参数可以是多个，
所以获得的是一个列表（list)，也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。
其第一个元素是程序本身，随后才依次是外部给予的参数。
"""
import sys

a = sys.argv[0]  # sys.argv[0]为程序运行的全路径名
print('sys.argv[0]', a)
# print(sys.argv[2],sys.argv[1])

# 3.sys.modules
"""
sys.modules:已加载的模块字典
sys.modules是一个全局字典，该字典是python启动后就加载在内存中。
每当导入新的模块，sys.modules都将记录这些模块。字典sys.modules对于加载模块起到了缓冲的作用。
当某个模块第一次导入，字典sys.modules将自动记录该模块。
当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度

一:存在模块B
 1.sys.modules 有B这个键,
 2.从B.__dict___查找
二:不存在模块B
 1.sys.modules 不存在这个键，会创建这个模块
 2.对象此时其__dict__为空
 3.执行B.py 以填充__dict__
 4.从B.__dict__查找
"""

# 4.系统编码
print(sys.getfilesystemencoding())

# 5.os.environ:用来获取当前操作系统的一些基本信息
"""
window:
    os.environ['HOMEPATH']:当前用户主目录。
    os.environ['TEMP']:临时目录路径。
    os.environ["PATHEXT"]:可执行文件。
    os.environ['SYSTEMROOT']:系统主目录。
    os.environ['LOGONSERVER']:机器名。
    os.environ['PROMPT']:设置提示符。
linux:
    os.environ['USER']:当前使用用户。
    os.environ['LC_COLLATE']:路径扩展的结果排序时的字母顺序。
    os.environ['SHELL']:使用shell的类型。
    os.environ['LAN']:使用的语言。
    os.environ['SSH_AUTH_SOCK']:ssh的执行路径。
"""
print(os.environ)
# 给当前系统信息添加一个键值对
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xxx.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "xxx.settings"
os.putenv("DJANGO_SETTINGS_MODULE","xxx.settings")
# 获取
print(os.environ["DJANGO_SETTINGS_MODULE"])
print(os.environ.get("DJANGO_SETTINGS_MODULE"))
print(os.getenv("DJANGO_SETTINGS_MODULE"))
# 删除
del os.environ['DJANGO_SETTINGS_MODULE']
# 是否存在
if "DJANGO_SETTINGS_MODULE" in os.environ:
    pass

