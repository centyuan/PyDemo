import requests
import json

login_url = "https://www.wbtbest.info/login.php"

login_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
    "origin": "https://www.wbtbest.info",
    "referer": "https://www.wbtbest.info/zh-cn/index.php"
}
login_data = {
    "loginName":"hhhh5555",
    "password":"Xiang202122",
    "platform":1,
    "application":0,
    "deviceId":"Chrome 99",
}
response = requests.post(url=login_url,data=login_data,headers=login_headers,verify=False)
print(response.text)
# request.utils.dict_from_cookiejar从CookieJar对象返回一个dict
print("----------",requests.utils.dict_from_cookiejar(response.cookies)) # response.cookies返回RequestsCookieJar对象
re_cookie = requests.utils.dict_from_cookiejar(response.cookies)
bank_url = "https://www.wbtbest.info/uc/user/withdraw/banks/list/retrieve.php"
bank_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
    "origin": "https://www.wbtbest.info",
    "referer": "https:/www.wbtbest.info/zh-cn/uc/user/withdraw.php",
}
bank_cookie ={
"_ga":"GA1.2.291801888.1654232274",
"_gid":"A1.2.791812940.1654232274",
"JSESSIONID":"7824FAC647F184392F04BD6C50B0C4FA",
"AWSALB":"QwAujyFye97zW9Gcc4UYVniaqMbdPUdEHsQ/vhqYAS4zFZQzqRqKivxUG0A/xsodaypH0Mi6oc4zAVdANwtohsgqCHyNCdT0H1kK/TRozcV29TdvC0RQwyN2Fe0n",
"AWSALBCORS":"QwAujyFye97zW9Gcc4UYVniaqMbdPUdEHsQ/vhqYAS4zFZQzqRqKivxUG0A/xsodaypH0Mi6oc4zAVdANwtohsgqCHyNCdT0H1kK/TRozcV29TdvC0RQwyN2Fe0n",

}
#re = requests.post(url=bank_url,headers=bank_headers,cookies=bank_cookie,verify=False)
re = requests.post(url=bank_url,headers=bank_headers,cookies=re_cookie,verify=False)
re_dict = json.loads(re.text)
print(re_dict.get("withdraw"))
