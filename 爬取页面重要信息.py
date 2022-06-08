import requests
import re
"""

# 实例之匹配电话号码
str = 'dsadasdgs031-1564653233adads2312-24644567dZDxz'
pat = '\d{3}-\d{8}|\d{4}-\d{7}'
print(re.compile(pat).findall(str))
"""
# 匹配qq
or_d = """Java技术群： 227270512 （人数：3000）Go开发者群（新）： 14718890861 （人数：2000）PHP开发者群： 460153241 （人数：2000）MySQL/SQL群： 418407075 （人数：2000）大数据开发群： 655154550 （人数：2000）Python技术群： 287904175 （人数：2000）人工智能深度学习： 456236082 （人数：2000）测试工程师群： 415553199 （人数：2000）前端开发者群： 410430016 （人数：2000）C/C++技术群(新)： 629264796 （人数：2000）Node.js技术群(新)： 621549808 （人数：2000）PostgreSQL数据库群： 539504187 （人数：2000）Linux运维技术群： 479429477 （人数：2000）Oracle数据库： 175248146 （人数：2000）C#/ASP.Net开发者： 630493968 （免费，人数：2000）数据分析师群： 397883996 （人数：2000）//更多请阅读：https://www.yiibai.com/python3"""
data = requests.get("https://www.yiibai.com/python3").text
pat = '[1-9]([0-9]{5,11})'
result = re.compile(pat).findall(data)
# qq号去重
qqlist = list(set(result))
# print(result)

# 匹配邮箱
import re
regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
html_content = "邮箱:centyuan@outlook.com qq邮箱：375319412@qq.com,gmail邮箱centyuan@gmail.com，可惜不 centyuan@163.com"
emails = re.findall(regex,html_content)
# print(emails)

# 匹配电报
# 匹配微信



from bs4 import  BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    <p> 【WhatsApp】+95 966 238 2270  【微信】：HKCC9990  【QQ】15130390 </p>
    <p> 【vx】：ccccc </p>
     <p> 【wx】：ccccc </p>
     <p> 【QQ】15130390 </p>
     <p> 【qq】15130390 </p>
     <p> 【微信】15130390 </p>
     <p> 【TG】15130390 </p>
     <p> telegram 电报  https://t.me/ay10086 </p>
     <a href="https://t.me/ay10086" rel="noopener nofollow ugc">https://t.me/ay10086</a>
     <a href="https://t.me/ay10086" rel="noopener nofollow ugc"> 电报:https://t.me/ay10086 </a>

</div>
</body>
</html>
"""

wx_key = ["微信","wx","vx",]
qq_key = ["QQ","qq"]
tg_key = ['TG','电报','telegram']
email_key = [r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"]

# html_doc = response.text
soup = BeautifulSoup(html_doc,'lxml')
ce_shi = " <p> 【vx】：ccccc </p>"

for label in soup.select('body div'):  # 一般是p标签 span标签 h1 h2...
    content = label.get_text()
    print(label)
    # for regex in wx_key:
    #     print(re.findall(regex, content))
    #     print(label)
    print('------------------')


# # 微信号,qq号，TG号，邮箱
# # 文字：wx vx QQ TG 电报 @

# import json
# def get_cdninfo(url):
#     """
#     :param url 域名或者ip
#     """
#     re_url = "http://192.168.8.242:8000/api/cdn"
#     data = {
#         "target":url
#     }
#     res = requests.post(re_url,data=json.dumps(data))
#     return res
# if __name__ == '__main__':
#     # www.2096.cc
#     res=get_cdninfo("www.jd.com")
#     result = json.loads(res.text)
#     if result.get("code") == '200':
#         data = result.get("data")
#         print(len(data))
#         print(data[9]) # cdn
#         print(data[10]) # 地址
#         re_cdn = str(data[9]).split()
#         for index,value in enumerate(re_cdn):
#             print(index,value)
#         print(str(re_cdn[4:]))





