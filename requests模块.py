#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-7 下午12:07

import requests
"""
使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。

使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。
"""


#1最基本的get请求
response = requests.get('http://www.baidu.com')

#2添加headers和参数
kw = {'wd':'centyuan'}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010',

}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get('http://www.baidu.com/s?',params=kw,headers=headers)
#response = requests.get('http://www.baidu.com/baidu?',params=kw,headers=headers)


# 查看响应内容，response.text 返回的是Unicode格式的数据
#print(response.text)
print(response.url)
#最基本post请求可以直接用post方法
response = requests.post('http://www.baidu.com/')

#可以传入data response = requests.post('http://www.baidu.com/',data=data)
#print(response.text)

#Cookies



#代理proxies

# 根据协议类型，选择不同的代理
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "http://12.34.56.79:9527",
}

response = requests.get("http://www.baidu.com", proxies=proxies)

print(response.text)
