# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/18 14:42

# request.scheme  # 代表请求的方案，http或https
# print(request, type(request))  # 请求对象
# print(request.method)  # 请求方式 GET
# print(request.path)  # 请求路径
# print(request.GET)  # 接收GET请求的参数 <QueryDict: {'name': ['lisi'], 'like': ['code', 'movie']}>
# print(request.POST)  # 接收POST请求的参数 字典对象,不包括上传文件
# print(request.COOKIES)  # cookies
# print(request.session)  # session
# print(request.FILES)  # 接收上传的文件 <MultiValueDict: {}>
# print(request.META.get("REMOTE_ADDR"))  # request.META 标准的字典，包含所有http首部
"""
CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
CONTENT_TYPE —— 请求的正文的MIME 类型。
HTTP_ACCEPT —— 响应可接收的Content-Type。
HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
HTTP_HOST —— 客服端发送的HTTP Host 头部。
HTTP_REFERER —— Referring 页面。
HTTP_USER_AGENT —— 客户端的user-agent 字符串。
QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
REMOTE_ADDR —— 客户端的IP 地址。
REMOTE_HOST —— 客户端的主机名。
REMOTE_USER —— 服务器认证后的用户。
REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
SERVER_NAME —— 服务器的主机名。
SERVER_PORT —— 服务器的端口（是一个字符串）
"""

# print(request.GET.get("name"))  # 获取一个value
# print(request.GET.getlist("like"))  # 获取多个value
# # QueryDict：类字典对象，可以存在相同的key
# request.user    一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户
# 一个 django.contrib.auth.users.User 对象, 表示当前登录用户.
# 如果当前没有用户登录, user 被设置成 django.contrib.auth.models.AnonymousUser 的一个实例.
# 你可以用 is_anonymous() 来区分登录用户和未登录用户.

