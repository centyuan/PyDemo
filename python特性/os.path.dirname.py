# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-29 上午11:07
import os

# os.environ.setdefault("PERSONAL_MODULE","")
print("获取当前文件的路径:", __file__)
path = "/home/data.csv"
print("获取文件名:", os.path.basename(path))
print("返回绝对路径:", os.path.abspath(__file__))
print('当前文件的目录:', os.path.dirname(__file__))
print("当前文件的目录的上一级目录:", os.path.dirname(os.path.dirname(__file__)))
print('分割文件和文明后缀:', os.path.splitext(path))  # ('/home/data', '.csv')#
print('返回一个路径和文件名的元组:', os.path.split(path))
print('测试文件是否存在:', os.path.exists(path))
"""
os.path.isfile('/etc/passwd')
os.path.isdir('/etc/passwd')
os.path.islink('/usr/local/bin/python3')
# 获取文件大小
os.path.getsize(path) 
os.path.getmtime(path)
# 用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
os.listdir(path)     
# os.walk 返回遍历
for root, dirs,files in os.walk(path):     
    for name in files:
        pass
"""
# path='/home/centyuan/PycharmProjects/py_test/image/HeadImages/'
# os.environ.setdefault("")
print("os.environ", os.environ)
print(os.getenv("APPDATA"))
# os.path.split 返回一个路径和文件名的元组
dirname, filename = os.path.split('D:\BaiduNetdiskDownload\python-demo\python特性\os.path.dirname.py')
print("-------", __file__, os.path.basename(__file__))

#
