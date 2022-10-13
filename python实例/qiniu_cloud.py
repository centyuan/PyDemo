import os
import time
from qiniu import Auth, put_file, put_data, etag, BucketManager
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url

# https://github.com/piglei/django-qiniu


class QiniuClient():
    # _instance_lock = threading.Lock()

    def __init__(self, access_key, secret_key, bucket_name, host):
        """

        @param access_key:
        @param secret_key:
        @param bucket_name: 空间名称
        @param host: 'http://rhgfuxxaz.hn-bkt.clouddn.com'
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.host = host
        self.encrypt_key = ''
        self.query_string = 'yuan'
        self.client = Auth(access_key, secret_key)
        # 回调
        policy = {
            'callbackUrl': 'http://your.domain.com/callback.php',
            'callbackBody': 'filename=$(fname)&filesize=$(fsize)'
        }
    def __new__(cls, *args, **kwargs):
        if not hasattr(QiniuClient, "_instance"):
            # with QiniuClient._instance_lock:
            if not hasattr(QiniuClient, "_instance"):
                QiniuClient._instance = object.__new__(cls)
        return QiniuClient._instance


    def file_upload(self, key, file_data=None, file_path=None):
        """
        文件上传:上传文件binary 或路径
        @param key: 上传文件的key:上传文件的路径+文件名称
        @param file_data:binary
        @param file_path:本地文件路径 二选一
        @return:(bool,'失败或成功')
        """
        try:
            token = self.client.upload_token(self.bucket_name, key, 3600 * 24)
            if file_data:
                ret, info = put_data(token, key, file_data)
                print('上传ret',ret)
                print('上传info',info)
                assert ret['key'] == key
                return True, '上传成功'
            else:
                ret, info = put_file(token, key, file_path, version='v2')
                assert ret['key'] == key
                return True, '上传成功'
        except Exception as e:
            print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
            return False, '上传失败'

    def file_url(self, key):
        """
        获取文件url
        @param key: 上传文件的key:上传文件的路径+文件名称
        @return: url
        """
        try:
            deadline = int(time.time()) + 3600  # 当前时间后一小时
            timestamp_url = create_timestamp_anti_leech_url(self.host, key, self.query_string, self.encrypt_key,
                                                            deadline)
            private_url = self.client.private_download_url(self.host+'/'+key,expires=300)
            print('private_url:',private_url)
            return timestamp_url
        except Exception as e:
            print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
            return None

    def file_delete(self, key):
        """
        删除文件
        @param key:上传文件的key:上传文件的路径+文件名称
        @return:
        """
        try:
            # 初始化BucketManager
            bucket = BucketManager(self.client)
            ret, info = bucket.delete(self.bucket_name, key)
            assert ret == {}
            return True, '删除成功'
        except Exception as e:
            print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
            return False, '删除失败'

    def get_key(self,type_name,filename):
        """

        @param type_name: 课程包名称|其他表名之类的
        @param filename: 文件名称
        @return:
        """
        import uuid
        name, name_suffix = str(filename).split('.')
        uuid = ''.join(str(uuid.uuid1()).split('-'))[:6]
        return type_name+'/'+name+uuid+'.'+name_suffix

access_key = "4EPFvB7wxfBI68faAxmtgfyeaNY4h7TB2D2t3VLC"
secret_key = "jpElWO1XZhLlxdvfFqtSsUV73Nu4RixxxraSk4Vr"
bucket_name = "abc-wen12"
host = 'http://rihlu8ghc.bkt.clouddn.com'

qiniu_client = QiniuClient(access_key, secret_key, bucket_name, host)
print('main外面')
if __name__ == '__main__':
    access_key = "4EPFvB7wxfBI68faAxmtgfyeaNY4h7TB2D2t3VLC"
    secret_key = "jpElWO1XZhLlxdvfFqtSsUV73Nu4RixxxraSk4Vr"
    bucket_name = "abc-wen12"
    host = 'http://rihlu8ghc.bkt.clouddn.com'
    qiniu_client = QiniuClient(access_key, secret_key, bucket_name, host)
    # localfile = "C:/Users/rainbow/Documents/剧本视频/剧本视频/游戏.mp4"
    # staus, info = qiniu_client.file_upload('可不.mp4', localfile)
    # file_data = open(localfile,'rb').read()
    # # staus, info = qiniu_client.file_upload('网络攻防进阶/clients_data.jpg',file_data,'')
    # result = qiniu_client.file_url('courseware/注销校园贷5df7cbc22478411ed9bb1000c29d2d2c0.mp4')
    # spath = r'C:Users\rainbow\Pictures\头像\avatar4.jpg'
    localfile_ = os.listdir("C:/Users/rainbow/Pictures/head/")
    keys = []
    # for name in localfile_:
    #     print(name)
    #     type_name = 'profile_photo'
    #     key = qiniu_client.get_key(type_name,name)
    #     keys.append(key)
    #     staus, info = qiniu_client.file_upload(key, file_path=os.path.join("C:/Users/rainbow/Pictures/头像/",name))
    #     print('上传返回:', staus, info)


    profile_photo_keys =[
        'profile_photo/avatar2e3b55e.jpg',
        'profile_photo/avatar3e3d233.jpg',
        'profile_photo/avatar4e58100.jpg',
        'profile_photo/avatar5e5bc0d.jpg',
        'profile_photo/avatar6e5dc29.jpg',
        'profile_photo/avatar7e606ea.jpg',
        'profile_photo/wallhaven-39gom9e624b9.jpg',
        'profile_photo/wallhaven-4g7yk3ec4456.jpg',
        'profile_photo/wallhaven-4v3d6lec6ab1.jpg',
        'profile_photo/wallhaven-4vdm7mec90fe.jpg',
        'profile_photo/wallhaven-4x6ypzed13c2.jpg',
        'profile_photo/wallhaven-d6x7gled5734.jpg',
        'profile_photo/wallhaven-ne39j8edb8c6.jpg',
        'profile_photo/wallhaven-v9v3r5eed1fd.jpg',
    ]
    for key in profile_photo_keys:
        result = qiniu_client.file_url(key)
        print(result)
    for key in profile_photo_keys:
        print(key)
    # print(qiniu_client.file_url('report_file/hh27bbc3f76e4a9a11edb827000c29d2d2c0.jpg'))