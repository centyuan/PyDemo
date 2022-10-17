import requests
import base64

# 本地图片
image_path = 'resource/JHU6.png'

with open(image_path, 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data),'utf-8') # base64编码图片
# 请求头
headers = {
         'Authorization': 'APPCODE 34b1a03ee87a413d8b6afb5922ff7df5',  # APPCODE +你的appcod,一定要有空格！！！
         'Content-Type': 'application/json; charset=UTF-8'         # 根据接口的格式来
    }


def aliyun_api():
    end_point = 'ocr-api.cn-hangzhou.aliyuncs.com'
    url_ = 'https://'+end_point +'?Action=RecognizeGeneral'
    files = {'file':open(image_path,'rb')}
    response = requests.post(url_,files=files,headers=headers)
    print(response.text)

if __name__=="__main__":

    aliyun_api()




# pip3 install aliyun-python-sdk-ocr