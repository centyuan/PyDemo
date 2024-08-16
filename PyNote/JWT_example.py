"""
JWT:json web token是无状态的,采用对称加密(),只需验证签名是否是自己签发的
有三部分组成:header.payload.signature
1.header:由token类型(JWT),算法名称(HS256),在base64
header = base64.b64encode({"alg":"HS256","typ":"JWT"}.encode("utf-8")
2.payload:记录存储简单的不重要的信息(信息是公开的),例如(用户名,id,过期时间)等,在base64
3.signature:用于验证签名信息算法被篡改
data = header的base64编码+payload的base64编码+secret(salt)
signature = 加密方式(data)
"""

# 1. pyjwt
"""
由于jwt是基于base64url编码，因此是可以反向解码的，所以一定要小心token泄漏的问题，以及不要在token中存放敏感数据

import jwt

headers = {
  "alg": "HS256",
  "typ": "JWT"
}
key = "asgfdgerher"
payload = {
  "name": "dawsonenjoy",
  "exp": int(time.time() + 1)
}
token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers).decode('utf-8')
info = jwt.decode(token, salt, True, algorithm='HS256')
"""
# 2. python-jose (pyca/cryptography)
# 密码哈希 Passlib
"""
生成秘钥: openssl rand -hex 32


"""

"""
azure_ad_verify_token
https://github.com/odwyersoftware/azure-ad-verify-token/blob/master/azure_ad_verify_token/verify.py
https://github.com/GeneralMills/azure-ad-token-verify/blob/main/aad_token_verify/token_verifier.py
https://robertoprevato.github.io/Validating-JWT-Bearer-tokens-from-Azure-AD-in-Python/

"""
# 3. JWT常见签名算法
1. HS256(HMAC with SHA-256)
HS256是一种对称加密算法，同一个秘钥用于签名和验证，可以使用OpenSSL生成一个随机的对称秘钥
```
# 随机生成一个32位16进制表示的随机数
openssl rand -hex 32
```
2.RS256(RSA Signature with SHA-256)
RS256是一种非对称加密算法，使用一对秘钥：私钥用于签名，公钥用于验签，可以使用OpenSSL生成RSA密钥对
```
# 生成 2048 位的私钥
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 从私钥生成公钥
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
3.ES256 (ECDSA with P-256 and SHA-256)
ES256 是一种基于椭圆曲线的数字签名算法，使用一对密钥：一个用于签名（私钥），另一个用于验证（公钥）,可以使用 OpenSSL 生成 EC（椭圆曲线）密钥对。
```
# 生成 EC 私钥（使用 prime256v1 曲线）：
openssl ecparam -genkey -name prime256v1 -noout -out private_key.pem
# 从私钥生成公钥
openssl ec -in private_key.pem -pubout -out public_key.pem
```
