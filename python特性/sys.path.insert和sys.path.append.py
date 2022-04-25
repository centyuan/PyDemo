#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-29 上午11:23
import sys
import os
#sys.path模块是动态的修改系统路径
#sys.path是python的搜索模块的路径集，是一个list
#Python解释器会自动将当前工作目录添加到sys.path

"""
Python import搜索的路径顺序
在程序中导入时，如下顺序
1、Python 标准库模块
2、Python 第三方模块
3、应用程序自定义模块

import的搜索顺序：
首先判断这个module是不是built-in即内建模块，如果是则引入内建模块，如果不是则在一个称为sys.path的list中寻找
sys.path在python脚本执行时动态生成，包括以下3个部分：
1、脚本执行的位置，即当前路径
2、环境变量中的PYTHONPATH, 即.bash_profilec.
3、安装python时的依赖位置
"""

print(sys.path) # sys.path.append("")备注:这个添加只是临时添加，如果退出当前会话，或者当前的shell，就会消失。
print("PATH",os.environ['PATH']) #os.environ["PATH"] += "新系统环境值"，
print("PYTHONPATH",os.environ['PYTHONPATH'])

sys.path.append('引用模块的地址')
sys.path.insert(0, '引用模块的地址') #优先与其他被important检查
print(sys.path)

