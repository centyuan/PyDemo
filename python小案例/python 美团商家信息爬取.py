#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-2 下午10:18

import csv
import xlwt
import time
import re
import requests
import json
import urllib.request

def main(page):
    store_list = []
    get_poiId(page,store_list)
    get_info(store_list)

def get_poiId(page,store_list):
    url = "http://haikou.meituan.com/meishi/b5313/pn" + str(page) + "/"
    print(url)
    header = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url, headers=header)
    html = response.text
    pattern = re.compile(r'{"poiId":.*?}', re.S)
    item_list = pattern.findall(html)  # 获取数据
    meituan_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    meituan_sheet = meituan_book.add_sheet('海口美团', cell_overwrite_ok=True)
    index = 0
    for data in item_list:
        index += 1
        dictinfo = json.loads(data)
        print(dictinfo)
        meituan_sheet.write(index, 1, dictinfo["title"])
        meituan_sheet.write(index, 2, dictinfo["address"])
        meituan_sheet.write(index, 3, dictinfo["poiId"])
        meituan_sheet.write(index, 4, dictinfo["avgScore"])
        meituan_sheet.write(index, 5, dictinfo["avgPrice"])
        store_list.append(dictinfo["poiId"])
    meituan_book.save("海口美团商户.xlsx")
    # csv_writer.writerow([dictinfo["title"], dictinfo["address"], dictinfo["avgScore"], dictinfo["avgPrice"]])

def get_info(store_list):
    print(store_list)
    info_url="http://haikou.meituan.com/meishi/"+str(store_list[5])+"/"
    print(info_url)
    headers= {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    req = urllib.request.Request(info_url, headers=headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(), 'utf-8')
    print(html)
    pattern = re.compile(r'{"poiId":.*?}', re.S)
    info_list = pattern.findall(html)  # 获取数据
    print(info_list)

    # meituaninfo_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # meituaninfo_sheet = meituaninfo_book.add_sheet('海口美团商家详细信息', cell_overwrite_ok=True)
    #
    # for data in info_list:
    #     index += 1
    #     store_list = json.loads(data)
    #     print(store_list)
    #     meituaninfo_sheet.write(index, 1, store_list["title"])
    #     meituaninfo_sheet.write(index, 2, store_list["address"])
    #     meituaninfo_sheet.write(index, 3, store_list["poiId"])
    #
    # meituaninfo_book.save("海口美团商家详细信息.xlsx")
    # pass

if __name__ == '__main__':
      main(1)


