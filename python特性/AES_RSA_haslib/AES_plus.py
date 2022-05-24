# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 20:45
import base64

from Crypto.Cipher import AES

BLOCK_SIZE = 16


def init_cipher(secret_key, iv_key):
    secret_bytes = secret_key.encode(encoding='utf-8')
    key_bytes = []
    #大于16
    if len(secret_bytes) >= BLOCK_SIZE:
        key_bytes = secret_bytes[:BLOCK_SIZE] #取前16个
    else:
        #小于16，后面补0
        key_bytes.extend(secret_bytes)
        key_bytes.extend([0 for x in range(0, BLOCK_SIZE - len(secret_bytes))])

    if iv_key is None or len(iv_key) == 0:
        cipher = AES.new(bytes(key_bytes), AES.MODE_ECB)
        return cipher
    else:
        iv_bytes = iv_key.encode(encoding='utf-8')
        iv_key_bytes = []
        if len(iv_bytes) >= BLOCK_SIZE:
            iv_key_bytes = iv_bytes[:BLOCK_SIZE]
        else:
            iv_key_bytes.extend(iv_bytes)
            iv_key_bytes.extend([0 for x in range(0, BLOCK_SIZE - len(iv_bytes))])

        cipher = AES.new(bytes(key_bytes), AES.MODE_CBC, bytes(iv_key_bytes))
        return cipher


def aes_encrypt(value, secret_key, iv_key):
    cipher = init_cipher(secret_key, iv_key)

    buffer = value.encode(encoding="utf-8")
    bufferList = list(buffer)
    # 数据进行 PKCS5Padding 的填充
    padding = BLOCK_SIZE - len(bufferList) % BLOCK_SIZE
    bufferList.extend([padding for x in range(0, padding)])
    buffer = cipher.encrypt(bytes(bufferList))
    #return buffer.hex()  # 使用hex格式输出
    return str(base64.b64encode(buffer), encoding='utf-8')


def aes_decrypt(value, secret_key, iv_key):
    cipher = init_cipher(secret_key, iv_key)
    #buffer = bytes.fromhex(value)  # 读取hex格式数据
    buffer = base64.b64decode(value)
    buffer = cipher.decrypt(buffer)
    result = buffer.decode("utf-8")

    # 去掉 PKCS5Padding 的填充
    return result[:-ord(result[len(result) - 1:])]


text = "克勤小物"
key = "123456"
iv = "abcdefg"

encryptText1 = aes_encrypt(text, key, iv)
print("【", text, "】经过【AES-CBC】加密后：", encryptText1)

decryptText1 = aes_decrypt(encryptText1, key, iv)
print("【", encryptText1, "】经过【AES-CBC】解密后：", decryptText1)

encryptText2 = aes_encrypt(text, key, None)
print("【", text, "】经过【AES-ECB】加密后：", encryptText2)

decryptText2 = aes_decrypt(encryptText2, key, None)
print("【", encryptText2, "】经过【AES-ECB】解密后：", decryptText2)