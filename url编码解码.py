# -*- coding:utf-8 -*-
from urllib.parse import quote_plus
from urllib import parse

datadict={
        'version':'1.0.0',     #接口版本号 不参与签名
        'merchantNo' : '300010068001',  # 平台商户号
        'pickupUrl' : 'http://baidu.com',  # 付款结果返回的前台接收地址
        'receiveUrl' : 'http://baidu.com',  # 付款结果返回的后台收地址
        'signType' : "MD5",  # 签名类型
        'orderTime' :"201808161810",  # 商户订单时间
        'orderNo' : '13143',  # 订单号
        'orderAmount' : '10',  # 订单金额(元)
        'orderCurrency' : 'CNY', #货币类型
        'customerId' : '',  # 平台客户号不参与签名
        'priv':'',    #商户保留域
        'sign' : '',  # 签名
    }

codestr='hello world'
codestr1='中文'
print(codestr.encode('utf-8'))
print(codestr1.encode('utf-8'))
print(quote_plus(codestr))
print(quote_plus(codestr1))
print(quote_plus('中文') )

url_data=parse.urlencode(datadict)#url编码
print('urlencode:',url_data)
print(parse.urlparse(url_data))#获取url参数 解码
url_org = parse.unquote(url_data) #解码url
print('urldecode:',url_org)
str1 = 'haha哈哈'
str2 = parse.quote(str1)   #quote()将字符串进行编码
print(str2,end='\n')                #str2=haha%E5%93%88%E5%93%88
#print(parse.urlencode(str1))
str3 = parse.unquote(str2) #解码字符串
print(str3)                #str3=haha哈哈

