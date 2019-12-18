# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/12/2 13:42

"""
Urllib和Urllib2是python2中提供的一个用于操作url的模块，但是提供了不同的功能。

在python2中，有urllib库和urllib2库。在python3中，urllib2被合并到urllib库中，在我们爬取网页的时候，经常用到这个库。

在Pytho2.x中使用import urllib2——-对应的，在Python3.x中会使用import urllib.request，urllib.error。
在Pytho2.x中使用import urllib——-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse
在Pytho2.x中使用import urlparse——-对应的，在Python3.x中会使用import urllib.parse。
在Pytho2.x中使用import urlopen——-对应的，在Python3.x中会使用import urllib.request.urlopen。
在Pytho2.x中使用import urlencode——-对应的，在Python3.x中会使用import urllib.parse.urlencode。
在Pytho2.x中使用import urllib.quote——-对应的，在Python3.x中会使用import urllib.request.quote。
在Pytho2.x中使用cookielib.CookieJar——-对应的，在Python3.x中会使用http.CookieJar。
在Pytho2.x中使用urllib2.Request——-对应的，在Python3.x中会使用urllib.request.Request。

"""
import urllib.request as urllib2
#  urllib2可以接受一个Request类的实例来设置URL请求的headers
url = ''
post_data = ''
req = urllib2.Request(url,post_data)
result = urllib2.urlopen(req)

data = result.read()  # 读取全部

dataline = result.readline()  # 读取一行内容

fhandle = open("./1.html", "wb")  # 将爬取的网页保存在本地
fhandle.write(data)

fhandle.close()


