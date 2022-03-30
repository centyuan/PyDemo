# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/1 21:26
"""
sys.modules是一个全局字典，该字典是python启动后就加载在内存中。
每当导入新的模块，sys.modules都将记录这些模块。字典sys.modules对于加载模块起到了缓冲的作用。
当某个模块第一次导入，字典sys.modules将自动记录该模块。
当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。

"""
import sys
def print_all():
    print(sys.modules)
    print(sys.modules[__name__])
print_all()
print(print_all.__name__)
print(__name__)
import os

print(os.environ)