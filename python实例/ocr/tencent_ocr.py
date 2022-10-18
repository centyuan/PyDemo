import base64
import json
import os
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.ocr.v20181119 import ocr_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


class TecentSdk:
    def __init__(self, api_key, secret_key, level=1):
        """
        创建client
        :param api_key:
        :param secret_key:
        :param level:识别级别(1:通用印刷识别,2:通用印刷体识别（高速版）3: 通用印刷体识别（高精度版）)
        """
        self.level = level
        self.cred = credential.Credential(api_key, secret_key)
        # 实例化一个http选项对象,可选的,
        self.httpProfile = HttpProfile()
        self.httpProfile.endpoint = 'ocr.tencentcloudapi.com'
        # 实例化一个client选项对象,可选的
        self.clientProfile = ClientProfile()
        self.clientProfile.httpProfile = self.httpProfile
        # 实例化client对象
        self.client = ocr_client.OcrClient(self.cred, 'ap-shanghai', self.clientProfile)
        # 实例化一个请求对象,每个接口都会对应一个request对象
        self.req = models.GeneralBasicOCRRequest()  # 1. 通用印刷体识别
        if level == 2:
            self.req = models.GeneralFastOCRRequest()  # 2.通用印刷体识别（高速版）
        elif level == 3:
            self.req = models.GeneralAccurateOCRRequest()  # 3. 通用印刷体识别（高精度版）
            # self.req = models.GeneralEfficientOCRRequest()  # 4. 通用印刷体识别（精简版） 效果最差

    def get_text(self, file_path=None, file_url=None):
        """
        识别验证码  file_path,file_url 二选一，都选默认file_path
        :param file_path: 图片路径
        :param file_url: 图片url
        :return: text
        """
        try:
            params = None
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    image_base64 = str(base64.b64encode(f.read()), 'utf-8')
                    params = {'ImageBase64': image_base64} if image_base64 else None
            elif file_url:
                params = {'ImageUrl': file_url}
            if params:
                # 载入参数
                self.req.from_json_string(json.dumps(params))
                # 返回一个GeneralEfficientOCRResponse的实例
                # 默认1 通用印刷体识别
                resp = self.client.GeneralBasicOCR(self.req)
                if self.level == 2:
                    resp = self.client.GeneralFastOCR(self.req)
                elif self.level == 3:
                    resp = self.client.GeneralAccurateOCR(self.req)
                    # resp = self.client.GeneralEfficientOCR(req)
                result = json.loads(resp.to_json_string())
                return True, result['TextDetections'][0]['DetectedText']
            else:
                return False, '图片为空'
        except TencentCloudSDKException as e:
            print(e.message, e.code)
            return False, e.message


if __name__ == '__main__':
    api_key = 'AKID02scCmLtJnDdyHbpvpW4stuoVxGMI1ob'
    secret_key = 'e8TRErLKOTYO3lkWFqLhsutlSyJkBX2R'
    tencent_client = TecentSdk(api_key=api_key, secret_key=secret_key, level=2)
    mark, text = tencent_client.get_text(file_path='resource/DYE.png')
    # mark, text = tencent_client.get_text(file_url='https://my.cnki.net/Register/CheckCode.aspx?id=1666067754366')
    print(text)
