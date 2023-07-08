#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-9 下午2:46
import requests
import re
import json

def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    html=request_dandan(url)
    items=parse_result(html)
    print(items)
    for item in items:
        write_itemToFile(item)

def request_dandan(url):
    try: #检查try语句中的错误，从而让except捕获异常 #如果你不想在异常发生时结束你的程序，只需在try里捕获它。
        response=requests.get(url)
        if response.status_code==200:
            return response.text
    except requests.RequestException:
          return  None

def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items: #yield当成return看
        yield {
            'rank',item[0],
            'image',item[1],
            'title',item[2],
            'recommend',item[3],
            'author',item[4],
            'times',item[5],
            'price',item[6],

        }
def write_itemToFile(item):
    print('开始写入数据===>'+str(item))
    with open('dangdang-bookrank.txt','a',encoding='UTF-8') as f:
        f.write(json.dumps(list(item),ensure_ascii=False) + '\n')
        f.close()

if __name__=='__main__':
    # for i in range(1,5):
    #     main(i)
    main(1)