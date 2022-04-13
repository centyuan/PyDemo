# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/4/1 20:47
from django.contrib.auth.models import User,AbstractUser
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
