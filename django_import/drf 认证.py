# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/4/1 23:48

# 常用的认证机制包括 session auth(即通过用户名密码登录)，basic auth，token auth和OAuth，服务开发中常用的认证机制为后三者。

'''
https://www.cnblogs.com/eric_yi/p/8422373.html
https://blog.csdn.net/qq_39253370/article/details/124633833
# url进入后的流程rest framework 逻辑层
1.as_view()            ->
2.cls.dispatch         ->
3.self.initialize_request:重新封装了request(
封装了：parsers(解析信息),authenticators(认证信息：默认的认证对象列表=>配置文件设置的DEFAULT_AUTHENTICATION_CLASSES),negotiator(协商信息),parser_context(解析内容)
)                     ->
4.self.initial():初始化被封装的reqeust:具体实现 版本处理，用户认证,权限,访问频率限制
                      ->
                      initial里面 self.perform_authentication(具体认证)：遍历认证对象列表，并执行对象的authenticate方法

5.dispatch中的initial方法执行完之后，会继续判断request.method并执行method相应的method.


authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
DEFAULT_AUTHENTICATION_CLASSES: 所有认证对象的列表
'''

# 一：认证设置
# 1.3种基本认证
# from rest_framework.authentication import BasicAuthentication
# authenticate认证成功返回(request.user,request.auth)=>(django user,None)

# from rest_framework.authentication import SessionAuthentication
# authenticate认证成功返回(request.user,request.auth)=>(django user,None)

# from rest_framework.authentication import TokenAuthentication
# authenticate认证成功返回(request.user,request.auth)=>(django user,rest_framework.authtoken.models.Token 实例)


# 2.自定义认证
# https://q1mi.github.io/Django-REST-framework-documentation/api-guide/authentication_zh/
# from rest_framework.authentication import BaseAuthentication
"""
要实现自定义的认证方案，
要继承BaseAuthentication类并且重写.authenticate(self, request) 方法。
如果认证成功，该方法应返回(user, auth)的二元元组，否则返回None

from rest_framework import authentication
class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        认证流程
        1.拿到用户模型User = get_user_model()
        2.将用户名密码取出来credentials = {
                    self.username_field: attrs.get(self.username_field),
                    'password': attrs.get('password')
                }
        3.调用authenticate方法将用户名密码传递过去
        4.使用_get_backends获取认证信息类(setting.py中配置的)
        5.使用jwt认证类下面的authenticate方法校验数据


"""
# 二:开启认证
# 1.设置全局的认证方案

# https://www.w3cschool.cn/lxraw/lxraw-bw2j35ou.html
REST_FRAMEWORK = {
    # 设置全局的默认身份验证方案.REST framework 将尝试使用列表中的每个类进行身份验证，并使用成功完成验证的第一个类的返回值设置 request.user 和request.auth
    """
    如果没有类进行验证，request.user 将被设置成 django.contrib.auth.models.AnonymousUser的实例，request.auth 将被设置成None。
    未认证请求的request.user 和 request.auth 的值可以使用 UNAUTHENTICATED_USER和UNAUTHENTICATED_TOKEN 设置进行修改
    """
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 设置权限策略
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

}

# 2.基于APIView类视图的方式，在每个view或每个viewset基础上设置身份验证方案。
"""
#基于类
#authentication_classes = (SessionAuthentication, BasicAuthentication)
#permission_classes = (IsAuthenticated,)
#基于函数的视图，那就使用@api_view装饰器。
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
"""

from rest_framework.authtoken.models import Token


# 创建Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# 五：权限
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import SAFE_METHODS  # 包含'GET', 'OPTIONS'和'HEAD'的元组

# 六：自定义权限
"""
要实现自定义权限，请继承BasePermission并实现其中的以下方法中的一个或两个
.has_permission(self, request, view)
.has_object_permission(self, request, view, obj)
"""
