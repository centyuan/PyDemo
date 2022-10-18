import requests


class TextinApi:
    def __init__(self,api_key,secret_key):
        self.url = 'https://api.textin.com/ai/service/v2/recognize'
        self.head = {
            'x-ti-app-id':api_key,
            'x-ti-secret-code':secret_key,
        }

    def get_text(self,file_path=None,file_url=None):
        pass