# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
import os

###  basic
path = "/home/data.csv"
print("获取当前文件的路径:", __file__)
print("返回绝对路径:", os.path.abspath(__file__))
print('当前文件的目录:', os.path.dirname(__file__))
print("当前文件的目录的上一级目录:", os.path.dirname(os.path.dirname(__file__)))
print("返回当前工作目录:",os.path.getcwd())
print("获取文件名:", os.path.basename(path))
print('返回分割文件和文明后缀:', os.path.splitext(path))  # ('/home/data', '.csv')#
print('返回路径和文件名的元组:', os.path.split(path))
print('测试文件是否存在:', os.path.exists(path))

"""
# os.path.split 返回一个路径和文件名的元组
dirname, filename = os.path.split('D:\BaiduNetdiskDownload\python-demo\python特性\os.path.dirname.py')
print("-------", __file__, os.path.basename(__file__))

# 判断是否是文件目录
os.path.isfile('/etc/passwd')
os.path.isdir('/etc/passwd')
os.path.islink('/usr/local/bin/python3')


# 用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
os.listdir(path)     
# os.walk 返回遍历
for root, dirs,files in os.walk(path):     
    for name in files:
        pass
"""
###  获取环境变量
print(os.getenv("APPDATA"))  # print("os.environ", os.environ)



###  获取文件大小的四种方式
#1. os.stat().st_size()
print("os.stat(file_path).st_size:",os.stat(path).st_size)

#2. pathlib.Path.stat().st_size()
from pathlib import Path
print("Path(file_path).stat().st_size:",Path(path).stat().st_size)

#3. os.path.getsize()
print("os.path.getsize():",os.path.getsize(path))

#4. seek()
with open(path, "r") as f:
    print("f.seek(0,os.SEEK_END):",f.seek(0, os.SEEK_END))