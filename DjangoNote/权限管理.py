# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 23:38
"""
Django为Article模型自动创建的4个可选权限名分别为:
查看文章(view): blog.view_article
创建文章(add): blog.add_article
更改文章(change): blog.change_article
删除文章(delete): blog.delete_article

#查看是否有权限
user1.has_perm('blog.add_article')
#获取所有权限
user1.get_all_permissions()
user1.get_group_permissions()
#一：创建权限
1. 在Model的meta属性中添加permissions。 然后migrate
class Article(models.Model):

    class Meta:
        permissions = (
            ('publish_article','是否能发文章'),
            ('commet_article','是否能评论'),
        )
2.使用ContentType程序化创建permissions。
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(article)
permission1 = Permission.objects.create(
    codename='publish_article',
    name='Can publish articles',
    content_type=content_type,
#二：授予权限
使用user.user_permissions.add()方法
myuser.user_permissions.add(permission1, permission2, ...)
#移除用户什么权限
myuser.user_permissions.remove(permission, permission, ...)
#三：验证权限
函数使用装饰器
from django.contrib.auth.decorators import permission_required
@permission_required('polls.can_vote')
基于类的视图
from django.contrib.auth.mixins import PermissionRequiredMixin
class MyView(PermissionRequiredMixin,View):
         permission_required = ('polls.can_open', 'polls.can_edit')
"""