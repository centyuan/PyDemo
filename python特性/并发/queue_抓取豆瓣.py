# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/21 8:56

from queue import Queue
from lxml import etree
import requests
import csv
"""
Queue.full() 表示队列满了返回True
Queue.put()
Queue.empty() 如果队列满了返回True
Queue.get(block=True, timeout=None)：从对列中移除并返回一个数据。当队列为空值，将一直等待。
Queue.task_done() 

"""

import threading
class GetData(threading.Thread):
    def __init__(self, page_queue, data_queue):
        super(GetData, self).__init__()
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {
            'User-Agent':"",
            'Cookie': '你的cookie'
        }

    def run(self):
        while True:
            if self.data_queue.empty() and self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        html = etree.HTML(requests.get(url, headers=self.headers).content.decode('utf-8'))
        comment_items = html.xpath('//div[@class="comment-item "]')
        for comment_item in comment_items:
            try:
                user = comment_item.xpath('.//span[2]/a/text()')[0]
                comment_time = comment_item.xpath('.//span[2]//span[3]/@title')[0]
                star = comment_item.xpath('.//span[2]//span[2]/@title')[0]
                content = comment_item.xpath('.//span[@class="short"]/text()')[0]
                self.data_queue.put((user, comment_time, star, content))
            except:
                continue
class SaveData(threading.Thread):
    def __init__(self, page_queue, data_queue):
        super(SaveData, self).__init__()
        self.data_queue = data_queue
        self.page_queue = page_queue

    def run(self):
        with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['user', 'comment_time', 'star', 'content'])

        while True:
            if self.data_queue.empty() and self.page_queue.empty():
                break
            user, comment_time, star, content = self.data_queue.get()
            print(self.data_queue.get())

            with open('data.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([user, comment_time, star, content])

def main():
    p_queue = Queue()
    d_queue = Queue()
    for page in range(25):
        url = f'https://movie.douban.com/subject/26752088/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        p_queue.put(url)
    for x in range(5):
        t1 = GetData(p_queue, d_queue)
        # t1.daemon = True
        t1.start()
        t2 = SaveData(p_queue, d_queue)
        # t2.daemon = True
        t2.start()