# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/12/2 12:55

import urllib, sys
import ssl
import requests
import urllib.request as urllib2
from urllib.parse import urlencode


host = 'https://phonecheck.market.alicloudapi.com'
path = '/phoneAuthentication'
method = 'POST'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path

bodys['idNo'] = '''350298189012083221'''
bodys['name'] = '''张三'''
bodys['phoneNo'] = '''13511112222'''
#post_data = urllib.urlencode(bodys)
post_data = urlencode(bodys)
request = urllib2.Request(url, post_data)
#request = requests.post(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)#根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
#response = requests.get(request)
content = response.read()
if (content):
    print(content)
