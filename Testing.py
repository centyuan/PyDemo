
import requests
import cv2
import numpy as np
"""
from PIL import Image
from io import BytesIO
response = requests.get()
image = Image.open(BytesIO(response.content)
"""
cookies = {
    'JSESSIONID': 'NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
}

headers = {
    'authority': 't8816.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'JSESSIONID=NR6gAhIwSMqz1yx1I-u6mTnb.undefined',
    'referer': 'https://t8816.com/aoMenTYCLoginWeb/app/home',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
response = requests.get('https://t8816.com/aoMenTYCLoginWeb/app/checkCode/image?38', cookies=cookies, headers=headers)
img = cv2.imdecode(np.fromstring(response.content,np.uint8),1)
cv2.imwrite("captcha.png",img)

cv2.imshow("11",img)
cv2.waitKeyEx()

# s = "Talk is cheap show me the code"
# print(s.upper())
# print("原始", s)
# print(s.split(" "))
# print("原始", s)
# print(s.isspace())


class A:
    _bar = "aa"
    def __init__(self):
        self.val = 1
        self._bar = "单下划线"
        self.__boo = "双下划线"

    def p(self):
        print(self.val, self._bar, self.__boo)

    def _pp(self):
        print(self.val, self._bar, self.__boo)

    def __ppp(self):
        print(self.val, self._bar, self.__boo)


class B(A):
    def __init__(self):
        self.val = 1


print(A._bar)
a = A()
print(a.val)
a._bar = "aaa"
print(a._bar)
print(a._pp())
# print(a.__boo)
b = B()
print(b.val)
print(b._bar)
# print(b._pp())
print(b.__dir__())

