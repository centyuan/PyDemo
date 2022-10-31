# 官方文档
# https://jpadilla.github.io/django-rest-framework-jwt/#additional-settings
# Django-DRF框架中认证与权限
# https://blog.51cto.com/u_15127659/4679882

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
