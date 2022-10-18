import json

import requests
import base64
from aip import AipOcr


def baidu_token(ak, sk, grant_type='client_credentials'):
    """
    获取授权token,expires_in有效期为30天
    :param ak:官网获取的SK
    :param sk:官网获取的AK
    """
    grant_type = grant_type
    # params = {'grant_type': grant_type, 'client_id': ak_, 'client_secret': ak_}
    headers = {'content_type': 'application/json'}
    request_url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type={grant_type}&client_id={ak}&client_secret={sk}'
    response = requests.get(request_url, headers=headers)
    if response:
        return True, response.json()
    if 'error' in response.json():
        return False, response.json()
    return False, None


def baidu_api(api_key, secret_key, file_path=None, file_url=None):
    """
    百度ocr api(general_basic:通用文字识别标准版,accurate_basic:通用文字识别高精度版)
    :param api_key: API Key
    :param secret_key:	Secret Key
    """

    # baidu_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    baidu_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    params = {}
    if file_path:
        # 二进制打开
        with open(file_path, 'rb') as f:
            img = base64.b64encode(f.read())
            params = {'image': img}
    elif file_url:
        # 图片url
        params = {'url': file_url}
    mark, result = baidu_token(api_key, secret_key)
    if mark:
        baidu_url_ = baidu_url + '?access_token=' + result['access_token']
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(baidu_url_, data=params, headers=headers)
        if response:
            return response.json()
    else:
        #  {'error_description': 'unknown client id', 'error': 'invalid_client'}
        return  result

class BaiduSdk:
    def __init__(self,app_id,api_key,secret_key):
        self.client = AipOcr(app_id,api_key,secret_key)

    def get_text(self,file_path=None,file_url=None):
        """
        识别验证码
        :param file_path:
        :param file_url:
        :return: {'words_result': [{'words': '6RS5'}], 'words_result_num': 1, 'log_id': 1581898086821811984}
        """
        if file_path:
            with open(file_path, 'rb') as f:
                image = f.read()
                # options 可选参数：CHN_ENG中英混合
                res_image = self.client.basicGeneral(image, options={'language_type': 'CHN_ENG'})
                result = json.loads(res_image)
                return True,result['words_result'][0]['words']
        elif file_url:
            res_url = self.client.basicGeneralUrl(file_url, options={'language_type': 'CHN_ENG'})
            return res_url


if __name__ == '__main__':
    app_id = '27962995'
    api_key = 'lfQvGPWiWaYcPGt90n58PVhx'  # AK
    secret_key = 'ind5NK0lUMFtAj87uMkcmQASF6IswIZh '  # Sk
    # result = baidu_api(api_key, secret_key,file_path='resource/6RS5.png')
    baidu_client = BaiduSdk(app_id=app_id,api_key=api_key,secret_key=secret_key)
    result = baidu_client.get_text(file_path='resource/DYEA.png')
    print('ss',result)
    #result = baidu_sdk(app_id, api_key, secret_key, file_path='resource/6RS5.png')
