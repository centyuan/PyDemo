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
        # print(browser.page_source)  # 获取动态页面
        ht_str = """
        <body>
        <div>
        <li>
        <i class="icon iconfont"></i>
        QQ:<a href="//wpa.qq.com/msgrd?v=3&amp;uin=2630741602&amp;site=qq&amp;menu=yes">2630741602</a>
        </li>
        </div>
        </body>
        """
        ht = browser.page_source
        soup = BeautifulSoup(ht_str, 'lxml')
        headers = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",}

        # soup = BeautifulSoup(res.text,'lxml')
        label_list = []
        for child in soup.body.descendants:
            print('++++++++++++')
            print("chilie.string:", child.string)   # 如果一个节点只包含一个文本节点，或者是只包含一个节点，那么可以使用该属性获取该文本节点的文本内容，
            print("child.get_text():", child.get_text())  # get_text()方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容
            print(child.strings)  # .strings 属性来获取其子孙节点的所有文本,返回的是一个迭代器 用for text in child.strings print(text)
            print(child.stripped_strings) # stripped_strings 和strings属性一样，但会去掉换行和空格
            # https://blog.csdn.net/fengzhen8023/article/details/82903257
            if child.string:
                print(child.name)
                print(child)
                label_list.append(child.string)
                print("#############")
            else:
                label_list.append(child.get_text())
        label_list = list(set(label_list))
        for label in list(set(label_list)):
            for regex in wx_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    if len(label) < 40:
                        wx_list.append(str(label).strip())
                        break
            for regex in qq_key:
                if re.findall(regex, label):
                    # print("正则:",regex,re.findall(regex, label))
                    if len(label) < 40:
                        qq_list.append(str(label).strip())
                        break
            for regex in tg_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    if len(label) < 40:
                        tg_list.append(str(label).strip())
                        break
            if re.findall(email_regex, label):
                # print(email_regex, label)
                if len(label) < 40:
                    email_list.append(label)
        print('label')
        print(label_list)
        print('匹配数据',list(set(wx_list)), list(set(qq_list)), list(set(tg_list)), list(set(email_list)))
        return list(set(wx_list)), list(set(qq_list)), list(set(tg_list)), list(set(email_list))

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
        return None

if __name__ == '__main__':
    get_importinfo("https://www.pop800.com/")
    # 无头浏览器
    url = "https://v663.me/pc/home"

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36", }
    #
    # res = requests.get("https://www.yedanrongqi.com.cn/",headers=headers)
    # print(res.text)


