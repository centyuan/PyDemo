#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-17 下午4:10
from selenium import webdriver
import time

#help(webdriver)支持那些浏览器
driver=webdriver.Chrome()
#driver1=webdriver.Chrome()
driver.get('https://www.baidu.com')#打开页面
#driver1.get('https://www.google.com')
"""
find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
还有一种
from selenium.webdriver.common.by import By
input=browser.find_element(By.ID,"q")
"""
input = driver.find_element_by_css_selector('#kw')#通过css类选择器获取响应元素 #kw id="kw"

input.send_keys("海南师范大学")#输入
#input.clear() 清空内容
button = driver.find_element_by_css_selector('#su')#
button.click()
#print(driver.page_source)#获取源代码
print(driver.current_url)#获取请求链接
#driver.get_cookies()
#input.text 获取文本的值

time.sleep(5)
driver.close() #关闭浏览器
