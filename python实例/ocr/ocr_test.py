"""
# https://blog.csdn.net/qq_41937821/article/details/124037025
tesserocr 基于tesseract做的一层python api封装
pip install **.whl

tesseract --list-langs
# 识别图片
tesseract ocr_test.png result.txt -l chi_sim

import tesserocr
from PIL import Image
image = Image.open('ocr_test.png')
txt = tesserocr.image_to_text(image,lang='chi_sim')
print(txt)

"""

import time
import tesserocr
from PIL import Image
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from retrying import retry
from io import BytesIO
import numpy as np


# retrying库是用来设置浏览器重登次数的，io库是用来获取图片的

def process_image(image):
    demo = image.convert('L')  # 图像转换成灰度图像
    arr = np.array(demo)  # 图像转换成多维数组
    threshold = 100  # 设置灰度阈值100
    arr = np.where(arr > threshold, 255, 0)  # 筛选 超过阈值的像素改为白色，不超过的像素改为黑色
    final_image = Image.fromarray(arr.astype('uint8'))  # 转为图像
    txt = tesserocr.image_to_text(image, lang='chi_sim')  # tesserocr 识别图像
    print('txt:', txt)
    result = re.sub(r'\W', "", txt)  # \W 匹配非字母,数字,下划线 等价于[^A-Za-z0-9_]  后替换
    print('re.sub:', result)
    return result


#  10次重登次数，返回false的时候就进行重试

@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login(browser):
    browser.get('https://captcha7.scrape.center/')
    # browser.find_element_by_css_selector('.el-input__inner').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 获取验证码图片
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    time.sleep(1)
    # 处理图片
    txt = process_image(image)
    time.sleep(2)
    # 输入验证码
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(txt)
    # 点击登录按钮
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.login').click()
    # 成功这个文本所在元素出现说明登录成功，页面保留10秒后退出浏览器
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False


if __name__ == '__main__':
    broswer = webdriver.Chrome(
        executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
    while True:
        login(broswer)
        import time

        time.sleep(3)
