# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

# 将中文和特殊符号进行编码，避免发生歧义,出现三个％
# 互联网上数据的都是以二进制的方式(字节类型)传输的
from urllib import parse
from urllib import request

# 1.urlencode( )把字典中的数据转化为URL编码数据
url = 'http://www.baidu.com/s?'
dict1 = {'wd': '百度翻译'}
url_data = parse.urlencode(dict1)
print(url_data)  # url_data：wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91
data = request.urlopen((url + url_data)).read()  # 读取url响应结果
data = data.decode('utf-8')  # 将响应结果用utf8解码（二进制解码成str)
print('urlencode data:', data)

# 2.parse_qs可以用于对字典进行解码（将URL编码转化为utf-8编码）
data = {"name": "Tom", "age": "12岁", "grade": "7年级"}  # 创建一个字典
qs = parse.urlencode(data)
print(parse.parse_qs(qs))  # 对字典进行解码
# 2.quote unquote 可对字符串进行编码处理（不能编码字典）
str1 = 'haha哈哈'
str2 = parse.quote(str1)  # 将字符串进行编码
print('quote:', str2)  # str2=haha%E5%93%88%E5%93%88
str3 = parse.unquote(str2)  # 解码字符串
print('unquote:', str3)  # str3=haha哈哈
