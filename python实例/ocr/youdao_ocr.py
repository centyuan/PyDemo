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
            'detectType': '',
            'imageType': '1',
            'langType': '',
            'img': None,
            'docType': 'json',
            'signType': 'v3',
            'appKey': api_key,
        }
    def truncate(self,file_path):
        if os.path.exists(file_path):
            with open(file_path,'rb') as f:
                image = f.read()
                q = base64.b64encode(image).decode('utf-8')
                return True,q
        else:
            return False,None
    def get_text(self, file_path=None):
        image = ''
        with open(file_path, 'rb') as f:
            image = f.read()
        self.data['curtime'] = str(int(time.time()))
        self.data['salt'] = str(uuid.uuid1())
        mark,q = self.truncate(file_path)
        if mark:
            signstr = self.api_key+q+self.data['salt']+self.data['curtime']+self.secret_key
            sign = hashlib.sha256(signstr.encode('utf-8')).hexdigest()
            self.data['sign'] = sign
            res = requests.post(self.youdao_url,self.data)
        else:
            return False,'图片不存在'