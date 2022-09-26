# import pyttsx3
#
# engine = pyttsx3.init()  # 创建对象
# rate = engine.getProperty('rate')  # 获取当前语速
# engine.setProperty('rate', 125)  # 重设语速
# volume = engine.getProperty('volume')  # 获取当前音量(最小为0，最大为1)
# engine.setProperty('volume',1.0)  # 在0-1之间
# voices = engine.getProperty('voices')  # 获取当前发音的详细信息
#
# engine.say('有志者，事竟成，破釜沉舟，百二秦关终属楚；苦心人，天不负，卧薪尝胆，三千越甲可吞吴')
# engine.say(
#     'I love three things in the world ,The sun,the moon and you , the sun for the day, the moon for the night and you forever')
# engine.save_to_file('音频保存为文件', 'audio_file')  # 音频保存为文件
# engine.runAndWait()
# import re
# import base64

# import requests
# url_ = "http://192.168.8.34/group1/M00/00/05/wKgIImLQ3feAXhf9AEDLLFxGssA073.mp4?token=d6ce15460d2db26094c8be17a9df8317&ts=1660641493"
# get_web = requests.get(url_)
# with open('web_file','wb+') as f:
#     f.write(get_web.content)


import time
import requests
from qiniu import Auth, put_file, etag, BucketManager
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url


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
    def file_upload(self, key, file_path):
        # try:
        # key = "teset/"+"test_logo.png"
        # key = up_path + file_name
        token = self.client.upload_token(self.bucket_name, key, 3600)
        ret, info = put_file(token, key, file_path, version='v2')
        assert ret['key'] == key
        return True, '上传成功'
        # except Exception as e:
        #     print('异常log', e.__traceback__.tb_frame.f_globals['__file__'], e, e.__traceback__.tb_lineno)
        #     return False, '上传失败'

    def file_url(self, key):
        try:
            # file_name 资源路径 key
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
    # access_key = "EoNKAHEYVwKqW8JoCj410S6G69akLMxr04M-eF73"
    # secret_key = "_TtnMMXwSlPTVmUKv9B2BlxG_EpbBXF-C_vi2jTO"
    # bucket_name = "elliot39"
    # host = 'http://rhgfuxxaz.hn-bkt.clouddn.com'
    # qiniu_client = QiniuClient(access_key,secret_key,bucket_name,host)
    # localfile = "C:/Users/rainbow/Pictures/v2w.jpg"
    # staus,info = qiniu_client.file_upload('client_test.jpg',localfile)
    # print('上传返回:',staus,info)
    # result = qiniu_client.file_url('client_test.jpg')
    # print('url地址:',result)
    # # http://rhgfuxxaz.hn-bkt.clouddn.com/client_test.jpg?sign=c224e0c4e489a30493ba07861203a01e&t=6322cabf
    # # staus,info = qiniu_client.file_delete('client_test.jpg')
    # # print('删除返回:',staus,info)
    # er = bin(1234)  # 0b10011010010
    # oc = oct(1234)  # 0o2322
    # he = hex(1234)  # 0x4d2
    # print(er,type(er),oc,type(oc),he,type(he))
    # # 0b10011010010 <class 'str'> 0o2322 <class 'str'> 0x4d2 <class 'str'>
    # print('二进制',int(er,2),sep=':')
    # print('八进制',int(oc,8),sep=':')
    # print('十六进制',int(he,16),sep=':')
    pass