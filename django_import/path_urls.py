from django.urls import path,re_path
views = None
urlpatterns = [
    path('rank/<int:number>',views),
    re_path('rank/(?P<pk>[0-9]+)?',views)
]