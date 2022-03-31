# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 22:13
"""
django 内置以下几中signal类型
1 Model_signals
pre_init  model对象执行其构造方法前，自动触发
post_init model对象执行其构造方法后，自动触发
pre_save  model对象保存前，自动触发
post_save  model对象保存后，自动触发
pre_delete  model对象删除前，自动触发
post_delete  model对象删除后，自动触发
m2m_changed   model对象使用m2m字段操作
class_prepared

2 Managemeng_signals
pre_migrate 执行migreate前
post_migrate  执行migreate后

3 Request/Response_signals
request_started 请求来到前
request_finished 请求结束后

4 Test_signals
setting_changed  配置文件改变时
template_rendered 模板执行渲染操作时
5 Datebase_Wrapped
connection_created 创建数据库连接时


from django.db.models.signals import post_save,finished
from django.dispathc import receiver
#对于每个唯一的dispatch_uid,接收器都只被信号调用一次
@receiver(post_save,sender=MyModel,dispatch_uid='my_unique_identifier')
def my_handler(sender,instance,**kwargs):
    print('hello world')
#装饰器
@receiver(request_finished)
def my_callback(sender,**kwargs):
    print('request finished')
#手动连接信号
request_finished.connect(my_callback)

#自定义信号
from django.dispatch import Signal
#定义信号
get_request_exception = Signal(providing_args=["request"])
#发送信号
def create_signal(request):
    url_path = request.path
    #发送
    get_request_exception.send(create_signal,path=url_path,time=time.strftime("%Y-%m-%d %H:%M:%S:))

@receiver(get_request_exception,sender=create_signal):
def my_callback(sender,**kwargs):
    pass
"""