from urllib import parse
from urllib import request
import os
import base64

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

# 3.base64
img_path = r'OcrGather/resource/5R86.png'
if os.path.exists(img_path):
    with open(img_path,'rb') as f:
        image_base64 = str(base64.b64encode(f.read()),'utf-8')
        print('image_base64:',image_base64)
