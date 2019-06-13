#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-3 上午11:28
import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None



if __name__ == '__main__':
     pass

