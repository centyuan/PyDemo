#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-19 下午8:17
import requests
from bs4 import BeautifulSoup
import xlwt
import time
from multiprocessing import Pool,Process

def main(url,headers):
    print(url)
    html=request_douban(url,headers)
    print('main-----')
    soup=BeautifulSoup(html,'lxml')
    print('main_soup')
    save_to_excel(soup)

def request_douban(url,headers):
    try:
        print('request_douban')
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            print('request_douban',response.status_code)
            return response.text
    except requests.RequestException:
        print('request_requestException', response.status_code)
        return None


def save_to_excel(soup):
    index=0
    movie_list=soup.find(class_="grid_view").find_all('li')#因为class是python的关键字，所以在写过滤时写成class_
    movie_book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    movie_sheet=movie_book.add_sheet('多进程豆瓣电影Top250',cell_overwrite_ok=True)
    if movie_sheet:
        movie_sheet.write(0, 0, '名称')
        movie_sheet.write(0, 1, '图片')
        movie_sheet.write(0, 2, '排名')
        movie_sheet.write(0, 3, '评分')
        movie_sheet.write(0, 4, '作者')
        movie_sheet.write(0, 5, '简介')

    for item in movie_list:
        index=index+1
        item_name=item.find(class_='title').string
        item_img=item.find('a').find('img').get('src')
        item_index=item.find(class_='').string
        item_score=item.find(class_='rating_num').string
        item_author=item.find('p').text #.get_text()
        #item_intr = item.find(class_='inq').string
        print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + 'item_intr' )
        if movie_sheet:
            movie_sheet.write(index+1,1,item_img)
            movie_sheet.write(index+1,2,item_index)
            movie_sheet.write(index+1,3,item_score)
            movie_sheet.write(index+1,4,item_author)
            #movie_sheet.write(index+1,5,item_intr)
    movie_book.save("多进程豆瓣电影250.xls")
    print('save_to_ex')





if __name__=="__main__":
    start=time.time()
    urls = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    pool=Pool(4)#创建相应的进程池
    for i in range(0,10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        pool.apply_async(main,args=(url,headers))
    pool.close()#不在创建进程
    pool.join()#让进程池的进程执行完毕再结束
