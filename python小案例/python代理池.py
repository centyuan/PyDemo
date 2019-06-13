#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-3 下午8:21
import requests
import re



def main():
    headers = {
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    proxies = {
        "http": "http://59.32.37.73:3128",
        "http": "http://183.62.37.164:8080",
        "http": "http://120.79.172.37:8118",

    }  # 代理池
    response = ""
    info_url = "http://haikou.meituan.com/meishi/" + str(42635502) + "/"
    print(info_url)
    try:
        response = requests.get(info_url,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


if __name__=="__main__":
    html=main()
    print(html)
    pattern = re.compile(r'{"poiId":.*?}', re.S)
    item_list = pattern.findall(html)  # 获取数据
    print(item_list)