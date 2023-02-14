# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/22 3:00

def byte_size(string):
    print(len(string.encode('utf-8')))


byte_size('')
byte_size('Hello world')  # 一个字母占用一个字节
byte_size("炳兮，你好")  # 中文一个字占用三个字节
