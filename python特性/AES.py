# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 19:26
from Crypto.Cipher import AES
import base64


class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')


    def pkcs7padding(self, text):
        """明文使用PKCS7填充 """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """ AES加密 """
        #cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher = AES.new(self.key,AES.MODE_ECB)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """AES解密 """
        #cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher = AES.new(self.key,AES.MODE_ECB)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode('utf-8')
        return text.rstrip(self.coding)


if __name__ == '__main__':
    key = 'ONxYDyNaCoyTzsp83JoQ3YYuMPHxk3j7'
    iv = 'yNaCoyTzsp83JoQ3'
    a = Encrypt(key=key, iv=iv)
    text = "asdf234!@#sdfe"
    print("待加密:", text)
    e = a.aes_encrypt(text)
    print("加密:", e)
    d = a.aes_decrypt(e)
    print("解密:", d)
