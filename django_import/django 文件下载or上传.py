# 1.HttpResponse
import os

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
    response = FileResponse(open('ssr.txt', 'rb'), as_attachment=True, filename='文件名.txt')
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

# 4.django 文件上传
"""

http://c.biancheng.net/view/8120.html
多个文件上传:
if request.FILES.getlist('filename'):
    for file in request.FILES.getlist('filename'):
        program = Program.objects.create(case=case, program=file, program_name=file.name)
        # file.name 文件名 file 文件内容
单一文件上传:
# 获取文件流对象UploadedFile对象 (django.core.files.uploadedfile.UploadedFile)
# UploadedFile.read（）：从文件中读取整个上传的数据。小心整个方法：如果这个文件很大，你把它读到内存中会弄慢你的系统。你可以想要使用chunks（）来代替，看下面；
# UploadedFile.chunks()：如果上传的文件足够大需要分块就返回真。默认的这个值是2.5M，当然这个值是可以调节的。
file = request.FILES['myfile']  
# file = request.FILES.get('myfile') 
filename = os.path.join(settings.MEDIA_ROOT,file.name) # 文件储存路径，应用settings中的配置，file.name获取文件名
# 方式1
with open(filename,'wb') as f:
    data = file.read()
    f.write(data)
# 方式2
with open(filename,'wb') as f:
    for chunk in file.chunks():
        f.write(chunk)

warning:
1.POST方法
2.request的<form>有属性enctype="multipart/form-data"
"""


# 5.django 大文件断点上传和下载
# 一:断点文件上传
# 刪除目录及以下文件
def deldir(dir):
    if not os.path.exists(dir):
        return False
    if os.path.isfile(dir):
        os.remove(dir)
        return
    for i in os.listdir(dir):
        t = os.path.join(dir, i)
        if os.path.isdir(t):
            deldir(t)  # 递归调用
        else:
            os.unlink(t)  # 删除文件
    os.removedirs(dir)  # 递归删除目录下面的空文件夹


# 1.上传分片
# https://blog.csdn.net/qq_42991509/article/details/126589444
def upload_chunk(request):
    file_name = request.POST.get('identifier')
    chunk_index = int(request.POST.get('chunknumber'))
    total_chunk = int(request.POST.get('totalchunks'))
    upload_file = request.FILES['myfile']
    file_path = os.path.join('chunk_file', file_name)
    chunk_path = os.path.join(file_path, chunk_index)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(chunk_path, 'wb+') as destination:
        for chunk in upload_file.chunks():
            destination.write(chunk)


# 2.合并分片
def merge_chunk(chunk_file_path, total_chunk):
    """
    :param chunk_file_path: 分片目录
    :param total_chunk: 总分片数
    """
    chunks_file = list(set(os.listdir(chunk_file_path)))
    if len(chunks_file) == total_chunk:
        # 所有的分片 必须按照分块顺序排序，否则 可能合并的文件顺序被打乱
        all_chunk_file = os.listdir(chunk_file_path)
        all_chunk_file.sort(key=lambda x: int(x))
        target_path = os.path.join('chunk_file', '原始文件名.zip')
        with open(target_path, 'wb+') as f:
            for chunk_ in all_chunk_file:
                chunk_path = os.path.join(chunk_file_path, chunk_)
                with open(chunk_path, 'wb+') as g:
                    data = g.read()
                    f.write(data)

# 二:断点文件下载
# https://blog.csdn.net/ALLENsakaru/article/details/109039465 
# 1.文件生成器,防止文件过大，内存溢出
def down_file_iterator(file_path,start_pos,chunk_size):
    with open(file_path,mode='rb') as f:
        f.seek(start_pos,os.SEEK_SET)
        content = f.read(chunk_size)
        yield content

# 2.断点下载
def breakpoint_download(request,filename):
    pass