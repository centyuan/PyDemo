"""
python web分为两部分:服务器程序和应用程序
服务器程序:负责对socket服务器进行封装,并对请求来的请求数据进行整理
应用程序:负责具体的逻辑(避免重复造轮子,才有了web框架)

客户端--nginx--socket--WSGI--Django(uwsgi根据请求调用Django工程的某个文件或函数)
对并发的支持取决于WSGI程序的实现
request对象线程隔离:
1.django请求进来,会返回一个WSGIHandler的实例(显示传递request参数对象)
2.django(使用wsgiref)创建一个HttpRequest(其实是一个WSGIRequest对象-由wsgiref)对象,
flask(使用werkzeug)全局的request对象(多个线程分别new 出多个相应的requeset对象)
怎么保证各自线程里调用的request就是对应的对象? werkzeug:Local,LocalStack类
用字典的方式实现该类实例对象的线程隔离(当前线程id作为key)
(request作为全局变量,使用了werkzeug.local.Local()对象)

"""

"""  
flask请求到响应流程:
1.请求过来,调用Flask.__call__,返回wsgi_app(environ,start_response)
2.生成request请求对象和请求上下文环境 ctx = self.request_context(environ)
3.请求预处理,错误处理以及请求到响应的过程,response = self.full_dispatch_requeset()
4.在full_dispatch_request里:1.preprocess_request:flask钩子,实现before_request,2.dispatch_request()请求分发
5.在full_dispatch_request里:dispatch_request到具体url下
6.在full_dispatch_request里:make_response()将view_function返回值生成响应response_class对象
"""
