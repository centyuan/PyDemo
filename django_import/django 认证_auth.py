# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/4/1 20:47

#http://c.biancheng.net/django/
from django.contrib.auth.models import User,AbstractUser,Group
from django.contrib.auth import authenticate # 用户认证
from django.contrib.auth import login,logout #登入 登出
from django.contrib.auth.models import Permission #权限

# authenticate如何实现的
# 1.__get_backends获取当前系统定义的认证后端，并以此迭代（系统默认的认证后端是ModelBackend）
#AUTHENTICATION_BACKENDS 可以自定义认证后端
from django.contrib.auth.backends import ModelBackend #django默认用户认证后端

#2.ModelBackend里使用get_user_model 获取当前系统定义的用户模型
# get_user_model()实际获取的是settings.AUTH_USER_MODEL指定的User model

#分页
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

# 校验用户登录
1：User 的实例对象拥有 is_authenticated() 方法，可以在用户登录时进行认证。如果是真正的 User 对象，返回值为 True，
usage:在后台用 request.user.is_authenticated()
2:from django.contrib.auth.decorators import login_required
usage:@login_required

#校验用户权限
1:user_username.has_perm('user.add_article')
  user_username.has_perm('user.change_article')
2:from django.contrib.auth.decorators import permission_required
usage:@permission_required

"""
