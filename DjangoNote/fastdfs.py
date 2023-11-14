"""
from fdfs_client.client import Fdfs_client, get_tracker_conf
创建
FDFS_CLIENT_CONF, FDFS_BASE_HOST, FDFS_SECRET

class FDFSStorage(Storage):
    '''fastdfs文件存储类'''

    def __init__(self, client_conf=FDFS_CLIENT_CONF, base_url=FDFS_BASE_HOST):
        self.client_conf = client_conf
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self, name, content):
        '''保存文件时使用'''
        # name:你选择上传的文件的名字
        # content:包含你上传文件内容的File对象

        # 创建一个Fdfs_client对象,该对象是用来将文件上传到fastdfs的类，需要为其指定一个配置文件
        # 配置文件client.conf是复制过来的，注意修改里面的base_path和tracker_server
        conf_path = get_tracker_conf(self.client_conf)
        client = Fdfs_client(conf_path)

        # 上传文件 到fastdfs系统中
        # upload_by_file上传指定文件
        res = client.upload_by_buffer(content.read(), file_ext_name=content.name.split(".")[-1])  # 根据内容上传文件，因为content是file对象，所以用这个方法

        # 上传成功的返回结果如下
        "{‘Group name‘: ‘group1‘, " \
        "‘Remote file_id‘: ‘group1/M00/00/02/CtM3BVr-k6SACjAIAAJctR1ennA809.png‘, " \
        "‘Status‘: ‘Upload successed.‘, " \
        "‘Local file name‘: ‘/Users/delron/Desktop/1.png‘, " \
        "‘Uploaded size‘: ‘151.00KB‘, ‘Storage IP‘: ‘10.211.55.5‘}"

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件失败')
        filename = res.get('Remote file_id')
        if isinstance(filename, bytes):
            filename = filename.decode()
        # 返回存储在fastdfs的文件名
        return filename

    def exists(self, name):
        '''Django判断文件名是否可用'''
        # 因为文件名是存储在fastDFS中的，所以在Django中不存在是否可用的问题，直接返回False即可
        return False

    def url(self, fileId):
        # name是save方法返回的filename
        # name加上nginx服务器地址，就可以构造出一个完整的图片url
        # 进行token+ts参数构建
        # 得到group0/后面的部分
        name = fileId
        fileId = fileId[fileId.find('/') + 1:]
        timestamp = str(int(time.time()))
        buff = fileId + FDFS_SECRET + timestamp
        m = hashlib.md5()
        m.update(buff.encode())
        return self.base_url + name+"?token=" + m.hexdigest()+"&ts="+timestamp
      def download_(self, file_id):
        # ‘Remote file_id‘: ‘group1/M00/00/02/CtM3BVr-k6SACjAIAAJctR1ennA809.png‘
        conf_path = get_tracker_conf(self.clent_conf)
        client = Fdfs_client(conf_path)
        print('app下载down', conf_path)
        result = client.download_to_buffer(file_id.encode())
        #     @return dict {
        #             'Remote file_id'  : remote_file_id,
        #             'Content'         : file_buffer,
        #             'Download size'   : downloaded_size,
        #             'Storage IP'      : storage_ip
        #         }
        return result

    def delete_(self, file_id):
        conf_path = get_tracker_conf(self.clent_conf)
        client = Fdfs_client(conf_path)
        result = client.delete_file(file_id.encode())
        # ('Delete file successed.', b'group1/M00/00/06/wKgIImL9k-uAEmmcBGIWm0et6DI327.apk', b'192.168.8.34')
        return result

fast._save(name=None, content=request.FILES.get('screen_picture'))
fast.url(match_team.team.avatar.name

"""