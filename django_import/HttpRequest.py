# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/31 21:31
from django.contrib.auth.models import User
from django.contrib.auth import authenticate #认证
from django.contrib.auth import logout
from django.contrib.auth.backends import ModelBackend

"""
django request(HttpRequest)
1  HttpRequest.scheme 　     请求的协议，一般为http或者https，字符串格式(以下属性中若无特殊指明，均为字符串格式)
2  HttpRequest.body  　　    http请求的主体，二进制格式。
3  HttpRequest.path             所请求页面的完整路径(但不包括协议以及域名)，也就是相对于网站根目录的路径。
4  HttpRequest.path_info     获取具有 URL 扩展名的资源的附加路径信息。相对于HttpRequest.path，使用该方法便于移植
5  HttpRequest.method               获取该请求的方法，比如： GET   POST .........
6  HttpRequest.encoding             获取请求中表单提交数据的编码。
7  HttpRequest.content_type      获取请求的MIME类型(从CONTENT_TYPE头部中获取)，django1.10的新特性。
8  HttpRequest.content_params  获取CONTENT_TYPE中的键值对参数，并以字典的方式表示，django1.10的新特性。
9  HttpRequest.GET                    返回一个 querydict 对象(类似于字典，本文最后有querydict的介绍)，该对象包含了所有的HTTP GET参数
10  HttpRequest.POST                返回一个 querydict ，该对象包含了所有的HTTP POST参数，通过表单上传的所有  字符  都会保存在该属性中。
11  HttpRequest.COOKIES  　     返回一个包含了所有cookies的字典。
12  HttpRequest.FILES  　　       返回一个包含了所有的上传文件的  querydict  对象。通过表单所上传的所有  文件  都会保存在该属性中。
　　                                             key的值是input标签中name属性的值，value的值是一个UploadedFile对象

13  HttpRequest.META                返回一个包含了所有http头部信息的字典
14  HttpRequest.session       中间件属性
15  HttpRequest.site　　      中间件属性
16  HttpRequest.user　　     中间件属性，表示当前登录的用户。

django Rest framework Request
request.data 是Request对象的核心属性,它会返回请求体中所有的解析内容。能够处理任何数据，如文件和表单数据并且对适用于POST、PUT、PATCH方式请求。
request.query_params  请求体中的查询参数
request.parsers 会返回当前解析类的list，如果用户通过parser_classes设置
request.user
request.authenticators
"""