from selenium import webdriver
import time


def get_keyinfo(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头浏览器
        browser = webdriver.Chrome(
            executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
            options=options)  # 调用带参数的谷歌浏览器
        browser.get(url)
        time.sleep(4)
        ht_page = browser.page_source
        print('页面源码',ht_page)
        browser.save_screenshot('screen_shot.png')
        browser.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/signin?next=%2F'
    get_keyinfo(url)
