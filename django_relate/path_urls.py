from django.urls import path,re_path
views = None
# https://zhuanlan.zhihu.com/p/105570722
urlpatterns = [
    path('rank/<int:number>',views),
    re_path('rank/(?P<pk>[0-9]+)?',views)
]