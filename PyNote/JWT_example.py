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
