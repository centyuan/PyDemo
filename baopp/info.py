import requests

cookies = {
    'JSESSIONID': 'NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
}

headers = {
    'authority': 't8816.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'content-length': '0',
    'content-type': 'application/json',
    # 'cookie': 'JSESSIONID=NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
    'origin': 'https://t8816.com',
    'referer': 'https://t8816.com/aoMenTYCLoginWeb/app/accountSettings?type=personInfo',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.post('https://t8816.com/aoMenTYCLoginWeb/app/getSiteAndLogin?2794.818155698271',

    cookies=cookies,
    headers=headers,
)

result = response.json()
member_info = result.get("member")
print(member_info.get("firstName"))
print(member_info.get("memberVipLevelId"))
print(member_info.get("levelType"))
print(member_info.get("balance"))



response3 = requests.get('https://t8816.com/aoMenTYCLoginWeb/app/withdrawal', cookies=cookies, headers=headers)
# print(response3.text)
