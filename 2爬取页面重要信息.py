import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

def get_importinfo(url):
    """
    :param url 页面路径
    :return  wx_list,qq_list,tg_list,email_list
    """
    try:
        wx_key = ["微信", "wx", "vx", "WX","VX"]
        qq_key = ["QQ", "qq"]
        tg_key = ['TG', '电报', 'telegram']
        email_regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
        wx_list, qq_list, tg_list, email_list = [], [], [], []
        # 无头浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头浏览器
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        # browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",options=options)  # 调用带参数的谷歌浏览器
        browser = webdriver.Chrome(executable_path=r"C:\Users\rainbow\Downloads\chromedriver_win32\chromedriver.exe",options=options)  # 调用带参数的谷歌浏览器
        # browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用带参数的谷歌浏览器
        browser.get(url)
        browser.implicitly_wait(10)  # 隐式等待时间为10秒
        # print('页面动态')
        # time.sleep(3)
        print(browser.page_source)  # 获取动态页面

        ht = browser.page_source
        soup = BeautifulSoup(ht, 'lxml')
        headers = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",}

        # soup = BeautifulSoup(res.text,'lxml')
        label_list = []
        for child in soup.body.descendants:
            # print("chilie.string:", child.string)
            # print("child.get_text():", child.get_text())
            if child.string:
                # print('++++++++++++')
                # print(child.name)
                label_list.append(child.string)
                # print("#############")

        for label in list(set(label_list)):
            for regex in wx_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    wx_list.append(label)
                    break
            for regex in qq_key:
                if re.findall(regex, label):
                    # print("正则:",regex,re.findall(regex, label))
                    qq_list.append(label)
                    break
            for regex in tg_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    tg_list.append(label)
                    break

            if re.findall(email_regex, label):
                # print(email_regex, label)
                email_list.append(label)
        print(wx_list,qq_list,tg_list,email_list)
        return wx_list, qq_list, tg_list, email_list

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
        return None

if __name__ == '__main__':
    get_importinfo("https://www.967802.com:1066/default.html#/")