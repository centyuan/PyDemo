from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
import re
import queue
import requests
import random
import time


def ver_url(url,url_queue):
    try:
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
            ]
        headers = {
            "User-Agent": random.choice(user_agent_list)
        }
        response = requests.get(url, headers=headers, timeout=2)
        if response.status_code == 200:
            url_queue.put(response.url)
    except Exception as e:
        print('超时', e)



def get_customer_url(url):
    try:
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15", ]
        index_headers = {
            "User-Agent": random.choice(user_agent_list)
        }
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头浏览器
        browser = webdriver.Chrome(
            executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
            options=options)  # 调用带参数的谷歌浏览器
        # browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用带参数的谷歌浏览器
        browser.get(url)
        time.sleep(5)
        html_doc = browser.page_source
        print(html_doc)
        customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
        match_url = [x.group() for x in re.finditer(customer_regex, html_doc)]
        pool = ThreadPoolExecutor(30)
        url_queue = queue.Queue()
        for it in match_url:
            pool.submit(ver_url(it,url_queue))
        return list(url_queue.queue)

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
        return None


if __name__ == '__main__':
    result = get_customer_url("https://www.1more.com/")
    print('返回',result)
    # for i in range(url_queue.qsize()):
    #     print(url_queue.get())