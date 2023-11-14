#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-4 上午10:20
import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
#requests.packages.urllib3.disable_warnings()#如果不加此句会有：InsecureRequestWarning: Unverified HTTPS request is being made
#html = requests.get(url,verify=False)
html=requests.get(url)
# print(dir(html))
station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', html.text)#[\u4e00-\u9fa5]+匹配中文
stations = dict(station)
# pprint(stations,indent=4)
# print(stations)