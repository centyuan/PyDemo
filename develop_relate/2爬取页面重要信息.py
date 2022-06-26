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
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头浏览器
        browser = webdriver.Chrome(
            executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
            options=options)  # 调用带参数的谷歌浏览器
        # browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用带参数的谷歌浏览器
        browser.get(url)
        # print('页面动态')
        time.sleep(5)
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
                    if len(label) < 40:
                        wx_list.append(label)
                        break
            for regex in qq_key:
                if re.findall(regex, label):
                    # print("正则:",regex,re.findall(regex, label))
                    if len(label) < 40:
                        qq_list.append(label)
                        break
            for regex in tg_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    if len(label) < 40:
                        tg_list.append(label)
                        break
            if re.findall(email_regex, label):
                # print(email_regex, label)
                if len(label) < 40:
                    email_list.append(label)

        print('匹配数据',wx_list,qq_list,tg_list,email_list)
        return wx_list, qq_list, tg_list, email_list

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
        return None

if __name__ == '__main__':
    # get_importinfo("https://www.yedanrongqi.com.cn/")
    # # 无头浏览器
    # url = "https://v663.me/pc/home"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36", }

    res = requests.get("https://www.yedanrongqi.com.cn/",headers=headers)
    print(res.text)


