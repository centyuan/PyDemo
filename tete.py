import requests

cookies = {
    'greypanel_token': 'c361b9cc94bb553d82b44dbf7fc8eb5a',
    'greypanel_time': '1657722791',
}

headers = {
    'authority': 'ctl.818vtrans.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'null',
    'content-type': 'application/json; charset=UTF-8',
    'accept': 'application/json;',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'lang': 'zh_TW',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ctl.818vtrans.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'greypanel_token=c361b9cc94bb553d82b44dbf7fc8eb5a; greypanel_time=1657722791',
}

json_data = {
    'ip': '222.209.208.166',
}

response = requests.get('https://ctl.818vtrans.com', cookies=cookies, headers=headers, json=json_data)
print(response.status_code,response.text,response.status_code)
