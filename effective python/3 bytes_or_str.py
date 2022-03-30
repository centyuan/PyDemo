#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-12 下午10:46

#在python3中有两种表示字符序列的类型,bytes和str,前者的实例包含原始的8位值,后者的实例包含Unicode字符
#在python2中分别叫str和Unicode,str包含原始的8位,Unicode包含Unicode字符

def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return  value

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value



