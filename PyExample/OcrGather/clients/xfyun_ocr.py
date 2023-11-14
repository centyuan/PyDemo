from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import json
import requests


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    """
    解析url
    :param requset_url:
    :return:
    """
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    return host, path, schema


def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    """
    鉴权 并返回request url
    :param requset_url:
    :param method:
    :param api_key:
    :param api_secret:
    :return:
    """
    host, path, schema = parse_url(requset_url)
    date = format_date_time(mktime(datetime.now().timetuple()))
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    """
    signature原始字段(signature_origin)则为：
        host: api.xf-yun.com
        date: Wed, 11 Aug 2021 06:55:18 GMT
        POST /v1/private/sf8e6aca1 HTTP/1.1
    """
    # 生成摘要
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    # 对摘要编码
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }
    return requset_url + "?" + urlencode(values)


def XFyunApi(app_id, api_key, secret_key, file_path=None, file_data=None):
    """
    :param app_id:
    :param api_key:
    :param secret_key:
    :param file_path:
    :param file_data:
    :return:
    """
    APPId = app_id  # 控制台获取
    APISecret = secret_key  # 控制台获取
    APIKey = api_key  # 控制台获取
    imageBytes = None
    if file_path:
        with open(file_path, "rb") as f:
            imageBytes = f.read()
    if imageBytes:
        url = 'https://api.xf-yun.com/v1/private/sf8e6aca1'
        body = {
            "header": {
                "app_id": APPId,
                "status": 3
            },
            "parameter": {
                "sf8e6aca1": {
                    "category": "ch_en_public_cloud",
                    "result": {
                        "encoding": "utf8",
                        "compress": "raw",
                        "format": "json"
                    }
                }
            },
            "payload": {
                "sf8e6aca1_data_1": {
                    "encoding": "jpg",
                    "image": str(base64.b64encode(imageBytes), 'UTF-8'),
                    "status": 3
                }
            }
        }
        request_url = assemble_ws_auth_url(url, "POST", APIKey, APISecret)

        headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}
        response = requests.post(request_url, data=json.dumps(body), headers=headers)
        tempResult = json.loads(response.content.decode())

        finalResult = base64.b64decode(tempResult['payload']['result']['text']).decode()
        finalResult = finalResult.replace(" ", "").replace("\n", "").replace("\t", "").strip()
        text = ''
        for item in eval(finalResult)['pages'][0]['lines'][0]['words']:
            text += item['content']
        return text


if __name__ == '__main__':
    app_id = "eb78ba1a"  # 控制台获取
    secret_key = "ZmM3Mjc4NjcyNjcyYmJiNGZmNmU5NmNh"  # 控制台获取
    api_key = "618642319dd26346780f676e9f9dfad9"  # 控制台获取
    text = XFyunApi(app_id, api_key, secret_key, file_path='../resource/ocr_test.png')
    print(text)
