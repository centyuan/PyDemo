import time

from gevent import monkey

monkey.patch_socket()

import gevent
import string
import random
import requests
from gevent.lock import Semaphore


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        # 随机产生10个小写字母
        yield base_url + ''.join(random.sample(string.ascii_lowercase,10))


def download(url, semaphore):
    with semaphore:
        gevent.sleep(2)
        yield f'url:{url}'
        # response = requests.get(url)
        # yield response.text


def chunked_requests(urls, chunk_size=100):
    # 限制并发为10
    semaphore = Semaphore(10)
    all_requests = [gevent.spawn(download, url, semaphore) for url in urls]
    for res in gevent.iwait(all_requests):
        yield res


base_url = 'http://127.0.0.1:9000/test?name='
start_time = time.time()
urls = generate_urls(base_url, 50)
res_futures = chunked_requests(urls)
res_data = [item.value for item in res_futures]
for item in res_data:
    # print('开始',next(item))
    for i in item:
        print('开始',i)
    print('结束')
