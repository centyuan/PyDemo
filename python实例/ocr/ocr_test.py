'''
tesserocr 基于tesseract做的一层python api封装
下载 testdata
下载tesserocr-2.5.2-cp36-cp36m-win_amd64.whl
pip install **.whl

tesseract --list-langs
# 识别图片
tesseract ocr_test.png result.txt -l chi_sim
'''

import tesserocr
from PIL import Image
image = Image.open('ocr_test.png')
txt = tesserocr.image_to_text(image,lang='chi_sim')
print(txt)
import time
import tesserocr
from PIL import Image
import re
from selenium import webdriver
# from retrying import retry
from io import BytesIO
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
# retrying库是用来设置浏览器重登次数的，io库是用来获取图片的

# 将处理验证码的方法封装成一个函数方便调用
def process_image(image):
    """
    图片处理函数提取出正确的验证码
    :param image: 验证码图片
    :return: 返回字符串
    """
    # demo = image.convert('L')
    # arr = np.array(demo)
    # threshold = 100
    # arr = np.where(arr > threshold, 255, 0)
    # final_image = Image.fromarray(arr.astype('uint8'))
    # txt = tesserocr.image_to_text(final_image)
    # result = re.sub(r'\W', "", txt)
    # return result
    txt = tesserocr.image_to_text(image, lang='chi_sim')
    print(txt)
    result = re.sub(r'\W', "", txt)
    return result

# 设置了10次重登次数，当函数返回结果为false的时候就进行重试
# @retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
# 设置登录函数
def login(browser):
# 模拟浏览器访问练习网址
    browser.get('https://captcha7.scrape.center/')
    # 找到用户名输入这个节点并输入admin用户名
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    # 同理，找到密码输入这个节点并输入admin
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    # 验证码节点
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 获取验证码图片
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    # 调用函数处理图片识别验证码
    txt = process_image(image)
    # 输入验证码
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(txt)
    # 点击登录按钮
    browser.find_element(By.CSS_SELECTOR, '.login').click()
    # 当登录成功这个文本所在元素出现说明登录成功，页面保留10秒后退出浏览器
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False

# 设置模拟chrome浏览器并调用登录函数
if __name__ == '__main__':
    broswer = webdriver.Chrome( executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")

    login(broswer)
