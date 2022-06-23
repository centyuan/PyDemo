import re
import requests
import json
from selenium import webdriver
import time
from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<li class="Sevli" open-window="https://www.vcag537.net/OnlineCS" op-width="550px" op-height="735px" op-resize="no" op-name="OCSCenter">
<div class="icon_rLiveService"></div>
<span>在线客服</span>
</li>
<a target="_blank" href="http://wpa.qq.com/msgrd?v=3&amp;uin=965722111&amp;site=qq&amp;menu=yes"><div class="boxBlock"><span class="qq-cont">965722111</span></div></a>
<a target="_blank" href="https://www.rbxxw.com/Chat/Chat?userID=&amp;userName="><span><i><span role="img" aria-label="customer-service" class="anticon anticon-customer-service"><svg viewBox="64 64 896 896" focusable="false" data-icon="customer-service" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M512 128c-212.1 0-384 171.9-384 384v360c0 13.3 10.7 24 24 24h184c35.3 0 64-28.7 64-64V624c0-35.3-28.7-64-64-64H200v-48c0-172.3 139.7-312 312-312s312 139.7 312 312v48H688c-35.3 0-64 28.7-64 64v208c0 35.3 28.7 64 64 64h184c13.3 0 24-10.7 24-24V512c0-212.1-171.9-384-384-384zM328 632v192H200V632h128zm496 192H696V632h128v192z"></path></svg></span></i>&nbsp;在线客服</span></a>
<img src="http://j3.wdyxa.com/mh-mgm/pc/scripts/images/pz.png" alt="">
</body>
</html>
"""
import random
# 匹配url
url = "https://www.yedanrongqi.com.cn/"
# url = "https://x663.me/pc/home"
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15", ]
headers = {
    "User-Agent": random.choice(user_agent_list)
}
options = webdriver.ChromeOptions()
options.add_argument('headless')  # 无头浏览器
browser = webdriver.Chrome(
    executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
    options=options)  # 调用带参数的谷歌浏览器
# browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用带参数的谷歌浏览器
browser.get(url)
time.sleep(5)
print(browser.page_source)  # 获取动态页面
ht = browser.page_source
soup = BeautifulSoup(ht, 'lxml')
print("页面",ht)
#  匹配绝大多数域名
#  domain_regex = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,11}'
# domain_regex_1 = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+(com|net|org|in|me)'
customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
# match_re = [x.group() for x in re.finditer(customer_regex,html_doc)]
match_url = [x.group() for x in re.finditer(customer_regex, ht)]
print("匹配结果:", match_url)
success_url = []

for it in match_url:

    try:
        response = requests.get(it,headers=headers,verify=False,timeout=2)
        if response.status_code == 200:
            success_url.append(response.url)
    except Exception as e:
        continue
print('success成功',success_url)


