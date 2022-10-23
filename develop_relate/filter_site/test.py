import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 无头
browser = webdriver.Chrome(
    executable_path=r"resource/chromedriver.exe",
    # options=options
)
url_ = 'https://1382.hu/#/hall/chess'
browser.get(url_)
time.sleep(3)
browser.maximize_window()
browser.save_screenshot('shot.png')
time.sleep(10)