import re
import requests
import json

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

# 匹配url
url = "https://www.vcag537.net/Home/Index"
# url = "https://x663.me/pc/home"
index_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}
resp = requests.get(url, headers=index_headers)
print("页面", resp.text)
#  匹配绝大多数域名
#  domain_regex = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,11}'
# domain_regex_1 = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+(com|net|org|in|me)'
customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
# match_re = [x.group() for x in re.finditer(customer_regex,html_doc)]
match_url = [x.group() for x in re.finditer(customer_regex, resp.text)]
print("匹配结果:", match_url)
success_url = []

for it in match_url:
    re = requests.get(it,verify=False)
    if re.status_code == 200:
        success_url.append(it)
print(success_url)


