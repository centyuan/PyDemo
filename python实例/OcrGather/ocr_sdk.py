from .clients import *

class Client():
    def __init__(self):
        self.client_sdks = {
            'aliyun': AliyunSdk,
            'tencent': TecentSdk,
            'baidu': BaiduApi,
            'textin': TextinApi,
            'youdao': YoudaoApi,
            'xfyun': XFyunApi,
            'tesseract': TesseractOcr,
        }
        for k,v in self.client_sdks.items():
            setattr(self,k,v)
