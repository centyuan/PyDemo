import requests

cookies = {
    'JSESSIONID': 'NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
}

headers = {
    'authority': 't8816.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'JSESSIONID=NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
    'origin': 'https://t8816.com',
    'referer': 'https://t8816.com/aoMenTYCLoginWeb/app/home?l=0',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'pNetwork': 'MAIN_WALLET',
}

response = requests.post(
    'https://t8816.com/aoMenTYCLoginWeb/app/getBalance?3489.2079821878165',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)
