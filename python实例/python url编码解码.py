from urllib import parse
from urllib import request

# 1.url编码解码
url = 'http://www.baidu.com/s?'
# unlencode()将字典{k1:v1,k2:v2}转化为k1=v1&k2=v2
url_data = parse.urlencode({'wd': '百度翻译'})  # url编码
url_org = parse.unquote(url_data)  # url解码
data = request.urlopen((url + url_data)).read().decode('utf-8')
print(data)

# 2.字符串编码解码
str2 = parse.quote('haha哈哈')  # 字符串编码
print(str2)
str3 = parse.unquote(str2)  # 字符串解码
print(str3)
