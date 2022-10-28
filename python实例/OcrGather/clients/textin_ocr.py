import os
import requests

class TextinApi:
    def __init__(self, api_key, secret_key,level=1):
        self.url = 'https://api.textin.com/ai/service/v2/recognize'
        self.head = {
            'x-ti-app-id': api_key,
            'x-ti-secret-code': secret_key,
        }

    def get_text(self, file_path=None, file_url=None):
        try:
            if os.path.exists(file_path):
                image = None
                with open(file_path, 'rb') as f:
                    image = f.read()

                resp = requests.post(self.url, data=image, headers=self.head)
                result = resp.json()['result']['lines'][0]
                return True, result['text']
            else:
                return False, '文件为空'
        except Exception as e:
            return False, e


if __name__ == '__main__':
    api_key = '20dca87e2e299c49307c10fdc3624199'
    secret_key = '2399c33699ede20b8034717c8f65e74b'
    client = TextinApi(api_key=api_key,secret_key=secret_key)
    mark, text = client.get_text(file_path='../resource/DYEA.png')
    print(text)