#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-19 下午5:21
#报错，待后续眼睛
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

bili_browser=webdriver.Chrome()
bili_browser.get("https://www.bilibili.com/")
# search_input=bili_browser.find_element_by_css_selector("#search-keyword")
# search_input.send_keys("国光")
# search_button=bili_browser.find_element_by_css_selector("#search-submit")
# search_button.clear()
#等待元素可操作时候再执行
input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))
input.send_keys("国光")
#submit.click()
index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
index.click()