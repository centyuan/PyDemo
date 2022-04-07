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
from rest_framework.authentication import BaseAuthentication
"""
要实现自定义的认证方案，
要继承BaseAuthentication类并且重写.authenticate(self, request) 方法。
如果认证成功，该方法应返回(user, auth)的二元元组，否则返回None
"""


#https://www.w3cschool.cn/lxraw/lxraw-bw2j35ou.html
#1:设置全局的认证方案
REST_FRAMEWORK = {
    #设置全局的默认身份验证方案
    #REST framework 将尝试使用列表中的每个类进行身份验证，并使用成功完成验证的第一个类的返回值设置 request.user 和request.auth
    """
    如果没有类进行验证，request.user 将被设置成 django.contrib.auth.models.AnonymousUser的实例，request.auth 将被设置成None。
    未认证请求的request.user 和 request.auth 的值可以使用 UNAUTHENTICATED_USER和UNAUTHENTICATED_TOKEN 设置进行修改
    """
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
    #设置权限策略
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

}

#2:基于APIView类视图的方式，在每个view或每个viewset基础上设置身份验证方案。
"""
#authentication_classes = (SessionAuthentication, BasicAuthentication)
#permission_classes = (IsAuthenticated,)
"""
#3：基于函数的视图，那就使用@api_view装饰器。
"""
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
"""


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