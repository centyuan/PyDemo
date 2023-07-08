import requests
import cv2
import numpy as np

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



def get_captcha():
    response = requests.get('https://t8816.com/aoMenTYCLoginWeb/app/checkCode/image?38', cookies=cookies,
                            headers=headers)
    img = cv2.imdecode(np.fromstring(response.content, np.uint8), 1)
    # cv2.imwrite("captcha.png", img)

    cv2.imshow("11", img)
    cv2.waitKeyEx()


def login_to(json_data: str = None):
    response = requests.post(
        'https://t8816.com/aoMenTYCLoginWeb/app/loginVerification?6683.565057152922',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.json())


if __name__ == '__main__':
    # get_captcha()
    """
    账号/密码/名字/卡号/vip等级/余额/AG流水
    """
    json_data = {
        'txtLoginCaptcha': '4',
        'txtLoginUsername': 'z17821994074',
        'txtLoginPassword': 'sqhy0563',
    }
    login_to(json_data)
