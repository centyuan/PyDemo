import requests
import json

# 登录
login_url = "https://www.wbtbest.info/login.php"
login_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
    "origin": "https://www.wbtbest.info",
    "referer": "https://www.wbtbest.info/zh-cn/index.php"
}
login_data = {
    "loginName":"qiankang",
    "password":"qiankang",
    "platform":1,
    "application":0,
    "deviceId":"Chrome 99",
}
response = requests.post(url=login_url,data=login_data,headers=login_headers,verify=False)
# request.utils.dict_from_cookiejar从CookieJar对象返回一个dict
# 获取banklist
bank_cookies = requests.utils.dict_from_cookiejar(response.cookies) # response.cookies返回RequestsCookieJar对象
bank_url = "https://www.wbtbest.info/uc/user/withdraw/banks/list/retrieve.php"
bank_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
    "origin": "https://www.wbtbest.info",
    "referer": "https:/www.wbtbest.info/zh-cn/uc/user/withdraw.php",
}

#re = requests.post(url=bank_url,headers=bank_headers,cookies=bank_cookie,verify=False)
bank_re = requests.post(url=bank_url,headers=bank_headers,cookies=bank_cookies,verify=False)
bank_dicts = json.loads(bank_re.text)
banks = bank_dicts.get("withdraw").get("bindingBankList")
for item in banks:
    print(item)
    print(item.get("mobileHash"),item.get("bankName"),item.get("bankBranch"),item.get("bankAccount"),item.get("accountName"))

# 获取余额，等级
balance_url = "https://www.wbtbest.info/uc/user/main/balance/retrieve.php"
balance_headers = {
    "origin": "https://www.wbtbest.info",
    "referer": "https://www.wbtbest.info/zh-cn/uc/user/withdraw.php",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
}
balance_re = requests.post(url=balance_url,headers=balance_headers,cookies=bank_cookies,verify=False)
re_dict = json.loads(balance_re.text)
user_data = re_dict.get("user")
print(user_data.get("loginName"),user_data.get("balance"),user_data.get("userLevel"))

