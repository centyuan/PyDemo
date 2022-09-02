import time

import requests
from qiniu import Auth, put_file, etag, BucketManager
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url

access_key = "EoNKAHEYVwKqW8JoCj410S6G69akLMxr04M-eF73"
secret_key = "_TtnMMXwSlPTVmUKv9B2BlxG_EpbBXF-C_vi2jTO"
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 空间名
bucket_name = "elliot39"
# 文件名
key = "test_logo.png"
# 生成token 指定过期时间
token = q.upload_token(bucket_name, key, 3600)
localfile = "C:/Users/rainbow/Pictures/v2w.jpg"
# 初始化Bucketmanager
bucket = BucketManager(q)

# 上传
# ret,info = put_file(token,key,localfile,version='v2')
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

# 获取文件信息
# ret,info = bucket.stat(bucket_name,key)
# print(info)
# assert 'hash' in ret
#


# # 抓取网络资源到空间
# url = "http://rhgfuxxaz.hn-bkt.clouddn.com/"+key
# print(url)
# new_key = "new_logo.png"
# ret,info = bucket.fetch(url,bucket_name,new_key)
# print(info)
# assert ret['key'] == new_key

# 生成时间防盗链
host = 'http://rhgfuxxaz.hn-bkt.clouddn.com'

encrypt_key = ''                    # 配置时间戳时指定的key

# file_name = 'teset/new_logo.png'  # 资源路径
# http://rhgfuxxaz.hn-bkt.clouddn.com/teset/new_logo.png?sign=d65ba3744bd934947a006a1cff27320c&t=630ed4a3
file_name = 'test_logo.png'
# http://rhgfuxxaz.hn-bkt.clouddn.com/test_logo.png?sign=35a482a596c988945e956be731773e13&t=630ed4bb

query_string = ''                    # 查询字符串,不需要加?
deadline = int(time.time()) + 3600   # 截止日期的时间戳,秒为单位，3600为当前时间一小时之后过期
timestamp_url = create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, deadline)
print(timestamp_url)

# 私有空间下载
base_url = "http://rhgfuxxaz.hn-bkt.clouddn.com/" + key
private_url = q.private_download_url(base_url, expires=3600)

print(private_url)
r = requests.get(private_url)
assert r.status_code == 200


# https://github.com/piglei/django-qiniu
#