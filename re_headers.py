import requests
import random
headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
    # "Referer":"https://www.w3cschool.cn/requests2/",
    # "Origin ":"10.31.2.5",
}
# url = 'http://httpbin.org/get'
# url = "http://ip.tool.chinaz.com/"
# url = 'http://httpbin.org/cookies'  #get
url = "http://httpbin.org/post"

cookies = {
    "PHPSESSID":"2dmi26tmggvr3oq4obj96pvke0",
    "kn_project_left_width":"279",
}
data = {
    "key1":'key1',
    "key2":'key2',
}

# 查看代理ip
# r = requests.get('http://httpbin.org/ip',proxies=proxy)
# print(r.text)


# response = requests.get("http://httpbin.org/get",proxies=proxy,headers=headers)
response = requests.post(url,data=data,cookies=cookies,headers=headers)
print(response.text)
print(response.request.headers)



