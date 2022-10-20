import base64
import hashlib
import os
import time
import uuid

import requests


class YoudaoApi():
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.youdao_url = 'https://openapi.youdao.com/ocrapi'
        self.data = {
            'detectType': '10012',  # 识别类型:按行是被(10012)
            'imageType': '1',  # 图片类型:1(Base64)
            'langType': 'en',  # zh-CHS:中文 zh-CHT:中文（繁体）en:英语
            'docType': 'json',
            'signType': 'v3',
            'appKey': api_key,
        }

    def truncate(self, q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

    def get_img_bs64(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                image = f.read()
                q = base64.b64encode(image).decode('utf-8')
                return True, q
        else:
            return False, None

    def get_text(self, file_path=None):
        self.data['curtime'] = str(int(time.time()))
        self.data['salt'] = str(uuid.uuid1())
        mark, q = self.get_img_bs64(file_path)
        if mark:
            signstr = self.api_key + self.truncate(q) + self.data['salt'] + self.data['curtime'] + self.secret_key
            sign = hashlib.sha256(signstr.encode('utf-8')).hexdigest()
            self.data['sign'] = sign
            self.data['img'] = q
            res = requests.post(self.youdao_url, self.data)
            result = res.json()
            if result['errorCode'] == '0':
                return True,result['Result']['regions'][0]['lines'][0]['text']
            return False,result['msg']
        else:
            return False, '图片不存在'


if __name__ == '__main__':
    api_key = '77f89e08f43a86f9'
    secret_key = 'HlmF4vlvwmemBL2tG4wIYiUob3BUjZQ1'
    client = YoudaoApi(api_key, secret_key)
    mark,text = client.get_text(file_path='resource/DYEA.png')
    print(text)
# {'msg': 'invalid appKey', 'requestId': '307e1704-ff6a-442e-9803-d26b69218753', 'errorCode': '108'}