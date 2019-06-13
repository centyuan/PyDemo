#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-5 下午3:34
from selenium import webdriver
import datetime
import time
driver=webdriver.Chrome()#创建一个chrome的实例
driver.get("https://www.taobao.com/")
driver.find_element_by_link_text("亲,请登录").click()

driver.get("https://cart.taobao.com/cart.htm")
time.sleep(4)
if driver.find_element_by_link_text("结算"):
    driver.find_element_by_link_text("结算").click()
