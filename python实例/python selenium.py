#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-17 下午4:10
from selenium import webdriver
import time

# help(webdriver)支持那些浏览器
broswer=webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
# driver1=webdriver.Chrome()
broswer.get('https://www.baidu.com')#打开页面
# driver1.get('https://www.google.com')

"""
定位节点方法
find_element_by_id()	通过 id 属性值定位
find_element_by_name()	通过 name 属性值定位
find_element_by_class_name()	通过 class 属性值定位
find_element_by_tag_name()	通过 tag 标签名定位
find_element_by_link_text()	通过<a>标签内文本定位，即精准定位。
find_element_by_partial_link_text()	通过<a>标签内部分文本定位，即模糊定位。
find_element_by_xpath()	通过 xpath 表达式定位
find_element_by_css_selector()	通过 css 选择器定位

"""
input = broswer.find_element_by_css_selector('#kw')  # 通过CSS id 选择器获取响应元素
input.send_keys("海南师范大学")#输入
# input.clear() 清空内容
# input.text 获取文本的值
# print(driver.page_source)  #获取源代码
print(broswer.current_url)#获取请求链接
broswer.get_cookies()
button = broswer.find_element_by_css_selector('#su')  # 通过CSS id 选择器获取响应元素 #
button.click()
broswer.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'#拉动进度条至底部
)
time.sleep(5)
broswer.close() #关闭浏览器

if __name__ == '__main__':
      # 不打开浏览器
      option = webdriver.ChromeOptions()
      option.add_argument('headless')  # 设置option
      driver = webdriver.Chrome(
            executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
            options=option)  # 调用带参数的谷歌浏览器
      driver.get("http://www.taobao.com")
      print(driver.page_source)  # 获取动态页面

import tesserocr
from PIL import Image
image = Image.open('ocr_test.png')
txt = tesserocr.image_to_text(image,lang='chi_sim')
print(txt)