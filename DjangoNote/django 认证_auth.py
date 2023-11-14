# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/4/1 20:47

# http://c.biancheng.net/view/8045.html
# https://blog.csdn.net/weixin_39934296/article/details/110773418
from django.contrib.auth.models import User, AbstractUser, Group
from django.contrib.auth import authenticate  # 用户认证
from django.contrib.auth import login, logout  # 登入 登出
from django.contrib.auth.models import Permission  # 权限

# authenticate如何实现的
# 1.__get_backends获取当前系统定义的认证后端，并以此迭代（系统默认的认证后端是ModelBackend,继承ModelBackend）
# AUTHENTICATION_BACKENDS 可以自定义认证后端
from django.contrib.auth.backends import ModelBackend  # django默认用户认证后端

# 2.ModelBackend里使用get_user_model 获取当前系统定义的用户模型
# get_user_model()实际获取的是settings.AUTH_USER_MODEL指定的User model

# 分页
"""
from django.core.paginator import Paginator
paginator = Paginator(queryset, 10)
paginator.count #分页的对象总数

paginator.num_pages #分页后的页面数
paginator.per_page #每一页的个数
paginator.page_range #分页后的页面范围
page2=paginator.page(2) #返回第二页的对象
page2.object_list #当前页上所有数据对象的列表
page2.number #当前页的序号
page2.paginator#当前page对象相关的Paginator对象，可通它可调用原有的Paginator属性
"""

"""
# auth模块总结
1.实现了了用户,用户组的增加 删除 更改功能
2.实现了用戶权限和用户组权限的增加 删除 更改功能
3.实现可以自定义用户权限和用户组权限
# 1. 自定义登录验证
# 方式1
from django.contrib.auth.backend import ModelBackend
class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = UserModel.objects.get(username=username)
        # if re.match(r'^1[3-9]\d{9}',username):
        #     UserModel.objects.get(username=username)  # 电话验证
        user = UserModel.objects.get(username=username,is_superuser=1)
        if user and user.check_password(password):
            return user
        elif user and user.password == password:
            return user
# 方式2
from django.contrib.auth.models import User
class EmailBackend(object):
    def authenticate(self, request, **credentials):
        #获取邮箱的认证信息即邮箱账号实例
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except Exception as error:
            print(error)
        else:
            #检查用户密码
            if user.check_password(credentials["password"]):
                return user
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except Exception as e:
            print(e)
            return None
#自定义认证后端
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'user.backends.EmailBackend',
] 

# 2.校验用户登录
1：User 的实例对象拥有 is_authenticated() 方法，可以在用户登录时进行认证。如果是真正的 User 对象，返回值为 True，
usage:在后台用 request.user.is_authenticated()
2:from django.contrib.auth.decorators import login_required
usage:
@login_required() # 参数login_url='/login/'
def index(request):
    pass
#3.校验用户权限
1:user_username.has_perm('user.add_article')
  user_username.has_perm('user.change_article')
2:from django.contrib.auth.decorators import permission_required
usage:@permission_required

"""
# JWT认证，自定义电话认证，自定义登录，修改payload
# https://blog.csdn.net/qq_41475058/article/details/113405639
# JWT认证流程
# https://blog.csdn.net/qq_40887840/article/details/121628355
"""
1.由源码可以看到 obtain_jwt_token 相当于调用了 ObtainJSONWebToken.as_view()
2.登录时使用的是post方式提交，所以进入到了ObtainJSONWebToken的父类JSONWebTokenAPIView的post方法中，
3.然后 self.get_serializer 又使用了ObtainJSONWebToken中配置的 serializer_class: JSONWebTokenSerializer, 调用serializer.is_valid()方法，即JSONWebTokenSerializer的validate方法，
4.验证用户，JSONWebTokenSerializer的validate方法又使用了 django配置中的AUTHENTICATION_BACKENDS属性（自定义的话需要继承django默认的ModelBackend），来调用其类中的authenticate方法，验证用户使用允许登录。
5.验证成功后，调用jwt_response_payload_handler()方法，这个方法具体方法内容在JWT_RESPONSE_PAYLOAD_HANDLER配置项中(就是前面自定义的jwt响应内容配置项)

"""
# 官方文档
# https://jpadilla.github.io/django-rest-framework-jwt/#additional-settings
# Django-DRF框架中认证与权限
# https://blog.51cto.com/u_15127659/4679882