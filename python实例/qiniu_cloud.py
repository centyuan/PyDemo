import time

import requests
from qiniu import Auth, put_file, put_data, etag, BucketManager
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url

access_key = "EoNKAHEYVwKqW8JoCj410S6G69akLMxr04M-eF73"
secret_key = "_TtnMMXwSlPTVmUKv9B2BlxG_EpbBXF-C_vi2jTO"
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 空间名
bucket_name = "elliot39"
# 文件名即
file_name = 'test_logo.png'
# 路径+文件名
key = "teset_2/" + "test_logo.png"
# 采用post,切ret未能回调返回
policy = {
    'callbackUrl': 'http://47.103.53.141:8888/api/callback',
    'callbackBody': 'filename=$(fname)&filesize=$(fsize)'
}

# 生成token 指定过期时间
token = q.upload_token(bucket_name, key, 3600, policy)
localfile = "C:/Users/rainbow/Pictures/v2w.jpg"
# 初始化Bucketmanager
bucket = BucketManager(q)

# 1.上传
# ret, info = put_file(token, key, localfile, version='v2')
# print('上传ret', ret)
# print('上传info', info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

# 2.获取文件信息
# ret,info = bucket.stat(bucket_name,key)
# print('获取文件信息',info)
# assert 'hash' in ret


# 3.抓取网络资源到空间
# url = "http://rhgfuxxaz.hn-bkt.clouddn.com/"+key
# print(url)
# new_key = "new_logo.png"
# ret,info = bucket.fetch(url,bucket_name,new_key)
# print(info)
# assert ret['key'] == new_key

# 4.下载相关:生成时间防盗链
# host = 'http://rhgfuxxaz.hn-bkt.clouddn.com'
# encrypt_key = ''  # 配置时间戳时指定的key
# # file_name = 'teset/new_logo.png'  # 资源路径
# # http://rhgfuxxaz.hn-bkt.clouddn.com/teset/new_logo.png?sign=d65ba3744bd934947a006a1cff27320c&t=630ed4a3
# # file_name = 'test_logo.png'
# # http://rhgfuxxaz.hn-bkt.clouddn.com/test_logo.png?sign=35a482a596c988945e956be731773e13&t=630ed4bb
# file_name = 'teset/test_logo.png'
# query_string = ''  # 查询字符串,不需要加?
# deadline = int(time.time()) + 3600  # 截止日期的时间戳,秒为单位，3600为当前时间一小时之后过期
# timestamp_url = create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, deadline)
# print('timestamp_url:', timestamp_url)

# # 5.下载相关:私有空间下载文件
# base_url = "http://rhgfuxxaz.hn-bkt.clouddn.com/" + key
# private_url = q.private_download_url(base_url, expires=3600)
# print('private_url:', private_url)
# r = requests.get(private_url)
# assert r.status_code == 200


# https://github.com/piglei/django-qiniu

class QiniuClient():
    def __init__(self, access_key, secret_key, bucket_name, host):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.host = host  # 'http://rhgfuxxaz.hn-bkt.clouddn.com'
        self.encrypt_key = ''
        self.query_string = ''
        self.client = Auth(access_key, secret_key)
        # 回调
        policy = {
            'callbackUrl': 'http://your.domain.com/callback.php',
            'callbackBody': 'filename=$(fname)&filesize=$(fsize)'
        }

    # def file_upload(self, file_name, file_path, up_path=''):
    def file_upload(self, key, file_data=None,file_path=None):
        try:
            # key = "teset/"+"test_logo.png"  key:路径+名称
            token = self.client.upload_token(self.bucket_name, key, 3600)
            if file_data:
                ret, info = put_data(token, key, file_data)
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
        try:
            deadline = int(time.time()) + 3600  # 当前时间后一小时
            timestamp_url = create_timestamp_anti_leech_url(self.host, key, self.query_string, self.encrypt_key,
                                                            deadline)
            return timestamp_url
        except Exception as e:
            print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
            return None

    def file_delete(self, key):
        # 初始化BucketManager
        try:
            bucket = BucketManager(self.client)
            ret, info = bucket.delete(self.bucket_name, key)
            assert ret == {}
            return True, '删除成功'
        except Exception as e:
            print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
            return False, '删除失败'


if __name__ == '__main__':
    access_key = "EoNKAHEYVwKqW8JoCj410S6G69akLMxr04M-eF73"
    secret_key = "_TtnMMXwSlPTVmUKv9B2BlxG_EpbBXF-C_vi2jTO"
    bucket_name = "elliot39"
    host = 'http://rhgfuxxaz.hn-bkt.clouddn.com'
    qiniu_client = QiniuClient(access_key, secret_key, bucket_name, host)
    localfile = "C:/Users/rainbow/Pictures/v2w.jpg"
    # staus, info = qiniu_client.file_upload('client_test.jpg', localfile)
    file_data = open(localfile,'rb').read()
    staus, info = qiniu_client.file_upload('client_data.jpg',file_data,'')
    print('上传返回:', staus, info)
    result = qiniu_client.file_url('client_data.jpg')
    print('url地址:', result)
    # http://rhgfuxxaz.hn-bkt.clouddn.com/client_test.jpg?sign=c224e0c4e489a30493ba07861203a01e&t=6322cabf
    # staus,info = qiniu_client.file_delete('client_test.jpg')
    # print('删除返回:',staus,info)
