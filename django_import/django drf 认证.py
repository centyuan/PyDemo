# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/4/1 23:48

from rest_framework.authentication import BasicAuthentication
#authenticate认证成功返回(request.user,request.auth)=>(django user,None)
from rest_framework.authentication import SessionAuthentication
#authenticate认证成功返回(request.user,request.auth)=>(django user,None)
from rest_framework.authentication import TokenAuthentication
#authenticate认证成功返回(request.user,request.auth)=>(django user,rest_framework.authtoken.models.Token 实例)
#自定义认证
"""
要实现自定义的认证方案，
要继承BaseAuthentication类并且重写.authenticate(self, request) 方法。
如果认证成功，该方法应返回(user, auth)的二元元组，否则返回None
"""

REST_FRAMEWORK = {
    #设置认证方案
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
    #设置权限策略
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

}
from rest_framework.authtoken.models import Token
#创建Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#权限
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import SAFE_METHODS #包含'GET', 'OPTIONS'和'HEAD'的元组。
#自定义权限
"""
要实现自定义权限，请继承BasePermission并实现其中的以下方法中的一个或两个
.has_permission(self, request, view)
.has_object_permission(self, request, view, obj)
"""