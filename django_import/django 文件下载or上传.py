# 1.HttpResponse
from django.http import HttpResponse, StreamingHttpResponse, FileResponse


def file_download(request):
    f = open("ssr.txt", "rb")
    response = HttpResponse(f, content_type='application/octet-stream')  # 文件类型
    response['Content-Disposition'] = 'attachment; filename={}'.format("ssr.txt")
    return response


# 弊端:httpresponse对象初始化时会将文件内容载入内存：当文件过大时会大量占用服务器内存
# 优化:HttpResponse对象允许将迭代器作为传入参数,

# 2.SteamingHttpResponse用于将文件流发送给浏览器,文件下载建议使用SteamingHttpResponse
def file_download(request):
    response = StreamingHttpResponse(open("ssr.txt", 'rb'))
    response['content_type'] = "application/octet-stream"
    response['content_Disposition'] = 'attachment; filename=' + 'ssr.txt'
    return response


#  SteamingHttpResponse 源码：将传入对象转为迭代器，而不是一次性加载到内存

# 3.FileResponse 为文件传输优化的流类型
def file_download(request):
    response = FileResponse(open('ssr.txt', 'rb'))
    # as_attachment:是否提供文件下载还是在浏览器读取
    response = FileResponse(open('ssr.txt', 'rb'),as_attachment=True,filename='文件名.txt')
    response['content_type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment; filename=' + 'ssr.txt'
    return response


# output = io.BytesIO(result.get('Content'))
# output.seek(0)
# response = HttpResponse()
# response.write(output.getvalue())

# FileResponse源码：迭代器中每次一固定大小读取文件，默认值：block_size = 4096
# https://blog.csdn.net/gezi_/article/details/78176943
# https://blog.csdn.net/qq_37674086/article/details/113351603

"""
实际例子：
#1
# file_name = app_obj.name + str(int(time.time())) + '.apk'
# with open(file_name, 'wb') as f:
#     f.write(result.get('Content'))
# time.sleep(1)
# response = FileResponse(open(file_name, 'rb'))
# 2
# response = StreamingHttpResponse(result.get('Content'))  # 速度慢
# response = FileResponse(result.get('Content'))           #  速度慢

# 3.
output = io.BytesIO(result.get('Content'))
output.seek(0)
response = HttpResponse()
response.write(output.getvalue())
response['content_type'] = "application/octet-stream"
response['Content-Disposition'] = 'attachment; filename=' + str(app_name)
print('返回response', response, response['Content-Disposition'])
return response
"""

# django 文件上传
"""

http://c.biancheng.net/view/8120.html
多个文件上传:
if request.FILES.getlist('filename'):
    for file in request.FILES.getlist('filename'):
        program = Program.objects.create(case=case, program=file, program_name=file.name)
        # file.name 文件名 file 文件内容
单一文件上传:
file = request.FILES['myfile']  # 获取文件流对象file
# file = request.FILES.get('myfile') 
filename = os.path.join(settings.MEDIA_ROOT,file.name) # 文件储存路径，应用settings中的配置，file.name获取文件名
with open(filename,'wb') as f:
    data = file.file.read()
    f.write(data)
    
warning:
1.POST方法
2.request的<form>有属性enctype="multipart/form-data"
"""
