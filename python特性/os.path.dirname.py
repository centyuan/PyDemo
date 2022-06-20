#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-29 上午11:07
import os

# os.environ.setdefault("PERSONAL_MODULE","")
print(__file__) #获取当前文件的路径
print(os.path.abspath(__file__))#返回绝对路径
print('当前目录',os.path.dirname(__file__))#得到当前文件所在目录
print(os.path.dirname(os.path.dirname(__file__)))#再来一个就是目录的上一级
#os.path.join(path,name) 把目录和文件名合成一个路径
is_exists=os.path.dirname(__file__)

# path='/home/centyuan/PycharmProjects/py_test/image/HeadImages/'
# print(is_exists)
# print(os.path.exists(path))
# os.listdir(path)用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
# 它不包括 '.' 和'..' 即使它在文件夹中。
# print(os.listdir(path))
# print(os.path.join(path1,path2,path3))
#os.environ.setdefault("")
print("os.environ",os.environ)
print(os.getenv("APPDATA"))

#os.path.split 返回一个路径和文件名的元组
dirname,filename = os.path.split('D:\BaiduNetdiskDownload\python-demo\python特性\os.path.dirname.py')

print("-------",__file__,os.path.basename(__file__))