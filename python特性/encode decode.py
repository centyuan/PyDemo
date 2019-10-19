#！/usr/bin/python3

# author centyuan
# @time 19-9-15 下午3:57

'''
python3中对文本和二进制做了比较清晰的区分。python3默认编码为unicode，由str类型进行表示。
二进制数据使用byte类型表示，所以不会将str和byte混在一起。在实际应用中我们经常需要将两者进行互转
'''
#str -->(encode) -->bytes , bytes -->(decode) -->str
#参考:https://blog.csdn.net/m0_38080253/article/details/78841280

"""
python3中两种字符串类型：
str : unicode的呈现形式
bytes :字节类型，互联网上数据的都是以二进制的方式(字节类型)传输的

使用方法:
str 使用encode方法转化为 bytes
bytes 通过decode转化为 str
编码方式解码方式必须一样，否则就会出现乱码


python2中字符串有两种类型: 
unicode(显示格式）、str（存储格式）

在Python2中，字符串无法完全地支持国际字符集和Unicode编码。为了解决这种限制，Python2对Unicode数据使用了单独的字符串类型。要输入Unicode字符串字面量，要在第一个引号前加上’u’。

Python2中普通字符串实际上就是已经编码(非Unicode)的字节字符串。
python2 中定义字符串的时候，会自动将字符串转换为合适编码的字节字符串，比如中文：自动转换为utf-8编码的字节字符串

"""

import sys
print('目前系统编码为:',sys.getdefaultencoding())
name = '小帅'
print(type(name))
name1 = name.encode('utf-8')
print(name1) #编码成二进制

name2 = name1.decode('utf-8')
print(type(name2))
print(name2)