
#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-12 下午9:24
from bs4 import BeautifulSoup


html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story" id='story'>Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc)
#写在前面 遍历操作
for link in soup.find_all('a'):
    print(link.get('href'))
#print(soup.prettify())
print(soup.title) #1：tag对象，最重要的属性 name和attribute
print(soup.title.name)#name
print(soup.title.string)#得到里面内容
print(soup.title.parent.name)#父结点的name属性
print(soup.p)
print(soup.p['class'])#attribute:class属性
print(soup.p.attrs)#也可以直接”点”取属性, 比如: .attrs
#tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样
print(soup.a)#最后.取的方式只能获得当前的第一个tag a
print(soup.find_all('a'))#这个可以得到所有a标签
print(soup.find(id='link2'))
print(soup.get_text())##从文档中获取所有文字内容:
print(soup.select('body a'))
print(soup.select('title'))
#.contents 和 .children 属性仅包含tag的直接子节点.例如,<head>标签只有一个直接子节点<title>
#通过tag的 .children 生成器,可以对tag的子节点进行循环:

# for child in title_tag.children:
#     print(child)
    # The Dormouse's story