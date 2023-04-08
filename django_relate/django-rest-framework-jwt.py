"""
官方文档
https://jpadilla.github.io/django-rest-framework-jwt/#additional-settings
Django-DRF框架中认证与权限
https://blog.51cto.com/u_15127659/4679882
JWT:json web token是无状态的,采用对称加密(),只需验证签名是否是自己签发的
有三部分组成:header.payload.signature
1.header:由token类型(JWT),算法名称(HS256),在base64
header = base64.b64encode({"alg":"HS256","typ":"JWT"}.encode("utf-8")
2.payload:记录存储简单的不重要的信息(信息是公开的),例如(用户名,id,过期时间)等,在base64
3.signature:用于验证签名信息算法被篡改
data = header的base64编码+payload的base64编码+secret(salt)
signature = 加密方式(data)

"""
# 生成token
from rest_framework_jwt.settings import api_settings

# user = request.user
user = ''
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_DECODE_HANDLER
payload = jwt_payload_handler(user)
token = jwt_encode_handler(payload)

# 1.
from rest_framework_jwt.utils import jwt_decode_handler

token = ''
user_id = jwt_decode_handler(token=token).get('user_id')
# 2.
from rest_framework_jwt.settings import api_settings

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
t = jwt_decode_handler(token=token)

# 3. pip install pyjwt
import jwt

user_token = token
settings = ''
user_id = jwt.decode(jwt=user_token, key=settings.SECRET_KEY).get('user_id')
