# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 19:26
from Crypto.Cipher import AES
import base64

"""
对称加密:AES,DES(采用同一个秘钥加解密,计算量小,加密速度快)
非对称加密:RSA(采用公钥和私钥,加密时间长,速度慢,适用少量数据)

AES的区块长度固定为128位，密钥长度则可以是128 bit，192 bit 或256位 bit 。换算成字节长度，就是密码必须是 16个字节，24个字节，32个字节:
1. 在Python中进行AES加密解密时，所传入的密文、明文、秘钥、iv偏移量、都需要是bytes（字节型）数据。python 在构建aes对象时也只能接受bytes类型数据。
2. 当秘钥，iv偏移量，待加密的明文，字节长度不够16字节或者16字节倍数的时候需要进行补全。
ECB性能更快，CBC更安全
3. CBC模式需要重新生成AES对象，为了防止这类错误，写代码无论是什么模式都重新生成AES对象。

AES加密:明文+密钥+偏移量(IV)+密码模式(算法/模式/填充)
AES解密:密文+密钥+偏移量(IV)+密码模式
AES加密模式:
    电码本模式(ECB)
    密码分组链接模式(CBC)
    计算器模式(CTR)
    密码反馈模式(CFB)
    输出反馈模式(OFB)

AES和DES区别:主要区别在于加密过程,在DES中,将明文分为两半,在进一步处理,AES是整个块一起处理
首选AES:
AES加密速度更快，对内存需求较低,分组长度和密钥长度(密钥长度更长最大256,DES密钥长度只有56bit,用穷举法很难破解)设计灵活，安全性较高

   
"""


class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    def zeropadding(self, text):
        while len(text) % 16 != 0:
            text += '\0'
        return text

    def pkcs7padding(self, text):
        """明文使用chr(num)填充 """
        length = len(text)
        padding_size = length if (len(text.encode('utf-8')) == length) else len(text.encode('utf-8'))
        # 需要填充几位
        padding = 16 - padding_size % 16
        # ord 字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        padding_text = chr(padding) * padding  # chr 整数返回对应字符
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """ AES加密 """

        # cipher = AES.new(self.key, AES.MODE_CBC, self.iv)  #CBC模式
        cipher = AES.new(self.key, AES.MODE_ECB)  # ECB模式
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """AES解密 """
        # cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher = AES.new(self.key, AES.MODE_ECB)
        #   
        content = base64.b64decode(content)
        # 解密
        text = cipher.decrypt(content).decode('utf-8')
        print(text)
        # rstrip 删除text末尾指定的字符
        return text.rstrip(self.coding)

import base64

from Crypto.Cipher import DES


class ExpirationCheck:
    key = b")EOz@@P*"  # 密钥 8位或16位,必须为bytes
    des = DES.new(key, DES.MODE_ECB)

    @classmethod
    def encrypt(cls, text: str) -> str:
        padded_text = cls.padding(text)
        encrypted = cls.des.encrypt(padded_text.encode("utf-8"))
        return base64.b64encode(encrypted).decode()

    @classmethod
    def decrypt(cls, text: str) -> str:
        encrypted = base64.b64decode(text)
        decrypted = cls.des.decrypt(encrypted)
        return decrypted.decode().rstrip(" ")

    @classmethod
    def padding(cls, text: str) -> str:
        # Adding padding with space characters to make text multiple of 8
        while len(text) % 8 != 0:
            text += " "
        return text


# if __name__ == "__main__":
#     text = "2024-04-03"
#     print("Before encryption:", text)
#     e = ExpirationCheck.encrypt(text)
#     print("Encrypted text:", e)
#     d = ExpirationCheck.decrypt(e)
#     print("Decrypted text:", d)

 
if __name__ == '__main__':
    key = 'ONxYDyNaCoyTzsp83JoQ3YYuMPHxk3j7'
    print(len(key))
    iv = 'yNaCoyTzsp83JoQ3'
    a = Encrypt(key=key, iv=iv)
    text = "asdf234!@#sdfe"
    print("待加密:", text)
    e = a.aes_encrypt(text)
    print("加密:", e)
    d = a.aes_decrypt(e)
    print("解密:", d)
