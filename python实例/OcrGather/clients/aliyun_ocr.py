import json
import os
from typing import List
from Tea.core import TeaCore
from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class AliyunSdk:
    def __init__(self, access_key_id, access_key_secret,level=1):
        """
        创建client
        :param access_key_id:  您的 AccessKey ID
        :param access_key_secret:  您的 AccessKey Secret
        :param level: 识别级别(1:通用文字识别,2:全文识别高精版)
        """
        config = open_api_models.Config(access_key_id=access_key_id, access_key_secret=access_key_secret)
        # 访问的域名
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        # 生成client
        self.client = ocr_api20210707Client(config)
        self.level = level

    def get_text(self, file_path=None):
        """
        识别验证码
        :param file_path: 图片路径
        :return: text
        """
        # 读取文件
        if os.path.exists(file_path):
            body_ = StreamClient.read_from_file_path(file_path)
            # 实例化请求对象
            recognize_req= ocr_api_20210707_models.RecognizeGeneralRequest(body=body_)  # 通用文字识别
            if self.level ==2:
                recognize_req = ocr_api_20210707_models.RecognizeAdvancedRequest(body=body_)   # 全文识别高精版
            runtime = util_models.RuntimeOptions()
            # 返回response
            resp = self.client.recognize_general_with_options(recognize_req, runtime)
            result = json.loads(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
            data = json.loads(result['body']['Data'])
            return True, data['content']
        else:
            return False,'图片为空'

    async def get_text_async(self, file_path=None):
        """
        异步识别验证码
        :param file_path: 图片路径
        :return:
        """
        if os.path.exists(file_path):
            body_ = StreamClient.read_from_file_path(file_path)
            recognize_req = ocr_api_20210707_models.RecognizeGeneralRequest(body=body_)
            if self.level == 2:
                recognize_req = ocr_api_20210707_models.RecognizeAdvancedRequest(body=body_)
            runtime = util_models.RuntimeOptions()
            resp = await self.client.recognize_general_with_options_async(recognize_req, runtime)
            result = json.loads(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
            data = json.loads(result['body']['Data'])
            return True, data['content']
        else:
            return False,'图片为空'


if __name__ == '__main__':
    api_key = 'LTAI5tQAGXXQSPEjL2EGUG5Q'
    secret_key = 'DgosljBDbem8Qf6oSTNJusUWtZnDmt'
    aliyun_client = AliyunSdk(access_key_id=api_key, access_key_secret=secret_key)
    mark,text = aliyun_client.get_text(file_path='resource/S5J.png')
    print(text)
