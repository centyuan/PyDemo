from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64

public_key_path = r"/tempfile/rsa_public_key.pem"
private_key_path = r"/tempfile/rsa_private_key.pem"


# pip install pycryptodome -i https://mirrors.aliyun.com/pypi/simple
def generate_key():
    # 随机数生成
    random_generator = Random.new().read
    rsa = RSA.generate(2048, random_generator)
    # 生成私钥
    private_key = rsa.exportKey()
    print(private_key.decode('utf-8'))
    # 生成公钥
    public_key = rsa.publickey().exportKey()
    print(public_key.decode('utf-8'))
    with open(r'/tempfile/rsa_private_key.pem', 'wb')as f:
        f.write(private_key)

    with open(r'/tempfile/rsa_public_key.pem', 'wb')as f:
        f.write(public_key)


def get_key(key_file):
    with open(key_file) as f:
        data = f.read()
        key = RSA.import_key(data)
    return key


# 公钥加密
def encrypt_data(msg):
    public_key = get_key(public_key_path)
    cipher = PKCS1_cipher.new(public_key)
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode('utf-8')))
    print('encrypt_data', encrypt_text.decode('utf-8'))
    return encrypt_text.decode('utf-8')


# 私钥解密
def decrypt_data(encrypt_msg):
    private_key = get_key(private_key_path)
    cipher = PKCS1_cipher.new(private_key)
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), '解密失败')
    print('decrypt_data:', back_text.decode('utf-8'))
    return back_text.decode('utf-8')


# 验证加解密
def test_encrypt_decrypt():
    msg = "aleng.net"
    encrypt_text = encrypt_data(msg)
    decrypt_text = decrypt_data(encrypt_text)
    print('test_encrypt_decrypt:', msg == decrypt_text)


# 私钥签名
def rsa_private_sign(data):
    private_key = get_key(private_key_path)
    signer = PKCS1_signature.new(private_key)
    # 摘要
    digest = SHA.new()
    digest.update(data.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    signature = signature.decode('utf-8')
    return signature


# 公钥验签
def rsa_public_checksign(text, sign):
    publi_key = get_key(public_key_path)
    verifier = PKCS1_signature.new(publi_key)
    digest = SHA.new()
    digest.update(text.encode('utf-8'))

    return verifier.verify(digest, base64.b64decode(sign))


# 验证签名
def test_sign():
    msg = "genie.top"
    # 签名
    sign = rsa_private_sign(msg)
    print('test_sign:', rsa_public_checksign(msg, sign))


if __name__ == '__main__':
    generate_key()
    # 验证加密解密
    test_encrypt_decrypt()
    # 验证签名
    test_sign()
