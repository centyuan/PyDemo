#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-7 下午12:07
import requests
"""
使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。
使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。
"""

# 1最基本的get请求
response = requests.get('http://www.baidu.com')
# 2添加headers和参数
kw = {'wd':'centyuan'}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010',

}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get('http://www.baidu.com/s?',params=kw,headers=headers)
#response = requests.get('http://www.baidu.com/baidu?',params=kw,headers=headers)
print(response.text)
print(response.url)
print(response.headers)

# 3. 最基本post请求可以直接用post方法
response = requests.post('http://www.baidu.com/') # data=data
print(response.text)

# 代理proxies
"""
python3.8以下版本：
proxies{' 要请求网站的协议类型 ' , ' 代理服务器ip : 端口 '}

python3.8以上版本：
proxies{' 要请求网站的协议类型 ' , ' "代理服务器类型(http/https/socks5)://代理服务器ip : 端口 '}

"""
proxies = {
    "http": "http://12.34.56.79:9527", # 根据协议类型，选择不同的代理
    "https": "http://12.34.56.79:9527",
}
response = requests.get("http://www.baidu.com", proxies=proxies)
print(response.text)
print(response.headers) # 响应头
print(response.json())
print(response.request)
print(response.cookies) # 返回cookie
print(response.encoding)
print(response.request.headers)
print(response.request.url) # 请求地址
print(response.request.method) # 请求头
print(response.request.body)
print(response.raise_for_status())  #  失败请求(非200响应)抛出异常
print(response.history)

# 4. requests.session()
'''1.使用该session之前的cookie等参数,2.TCP长连接或者是复用TCP 优化了Http(tcp) Https(TLS)等握手行为'''
url1 =  "https://XX.XX.XX.XX/api/v2/cmdb/firewall/address"
url2 = "https://XX.XX.XX.XX/api/v2/cmdb/firewall/policy/1"
token = 'xxxxxxxxxxxxx'
header = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "Authorization": token
}
res1 = requests.get(url=url1, headers=header, verify=False)
res2 = requests.get(url=url1, headers=header, verify=False)


# 5. data json 参数区别
# 使用data传递数据报错，改为json解决
new_h = {
            'authority': 'j9bcrest.com',
            'x-request-domain': 'j9con.com',
            'accept-language': 'cn',
            'sec-ch-ua-mobile': '?0',
            'display-language': 'cn',
            'authorization': 'aaaaaaaaaaaaaa',
            'product-id': 'HX1',
            'accept': 'application/json, text/plain, */*',
            'x-website-code': 'HX1_PC',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://j9con.com/',
        }

to_data = {'token': 'J9BC', 'value': 1, 'tradeCode': 'J9BC_USDT',
           }
to_url = 'https://www.j9bcrest.com/api/swap/open/calc/to'
to_res = requests.post(to_url, headers=new_h, json=to_data)
'''

在通过requests.post()进行POST请求时，传入报文的参数有两个，一个是data，一个是json。
data与json既可以是str类型，也可以是dict类型。
区别：
1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
3、data为str时，如果不指定content-type，默认为text/plain

4、json为dict时，如果不指定content-type，默认为application/json
5、json为str时，如果不指定content-type，默认为application/json

6、payloag 负载
用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式：表单形式
用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式：json形式

结论：一般给第三方发送报错json 格式错误 是因为第6点
https://zhuanlan.zhihu.com/p/202978890
https://zhuanlan.zhihu.com/p/530757412
#http://httpbin.org/
Content-Type：请求的数据的编码方式
application/x-www-form-urlencoded：浏览器原生 form 表单，如果不设置 enctype，最终提交数据时所用的就是这种编码方式
multipart/form-data：上传文件时所用的编码方式，在使用浏览器上传文件时，须将 form 表单的 enctype 字段设置为 multipart/form-data
application/json： JSON格式
text/xml：用于使用 XML 作为编码方式

'''
# files参数 文件上传
'''
1.将我们要上传的文件写为：
files = {"file": open(r"E:\test.xls", "rb")}
2.将我们在header里写的‘Content-Type’: 'multipart/form-data’去掉或者注释掉
因为request请求在做post请求时会自动加上Content-Type: multipart/form-data;boundary=${bound}，而我们在header里设置的并没有关键标识boundary

apk_file = open(str(program.program),'rb')
#['application/octet-stream', 'application/vnd.android.package-archive', 'application/x-zip-compressed', 'binary/octet-stream']
files = {
    "file":(program.program_name,apk_file,'application/octet-stream') # 
            文件名                 文件对象   编码方式
}
# files = {'file':open('文件路径','rb'} 用这个某些情况下有bug,用上面那种
res = requests.post(upload_url,files=files,headers=headers)

'''


