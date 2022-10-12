import time
from PIL import Image
from selenium import webdriver
import pytesseract

def get_captcha(driver):
    driver.save_screenshot('screen_shot.png')  # 截屏保存
    check_code = driver.find_element_by_id('phoneCheckCode')  # 找到验证码框
    left = check_code.location.get('x')
    top = check_code.location.get('y')
    width = check_code.size.get('width')
    height = check_code.size.get('height')
    right = width + left
    bottom = height + top
    print('位置,宽高', left,top,width,height)
    image = Image.open('screen_shot.png')  # 打开验证码文件
    captcha = image.crop((left, top, right, bottom))  # 根据位置裁剪
    captcha.save('captcha.png')  # 保存截取的验证码区域文件


def recognize_captcha(file):
    gray = Image.open(file).convert('L')  # 灰度化
    # gray.show()
    w, h = gray.size
    data = gray.load()  # 数值化，分配内存加载二维点阵数据
    for i in range(w):
        for j in range(h):  # 点阵里面的值，以128为界，置成0或者255.非黑即白
            if data[i, j] < 128:
                data[i, j] = 0
            else:
                data[i, j] = 255
            # print(data[i, j])

    return pytesseract.image_to_string(gray)  # pytesseract image_to_string 图像识别为字符串


if __name__ == '__main__':
    url = 'https://my.cnki.net/Register/CommonRegister.aspx'
    driver = webdriver.Chrome(
        executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
    driver.get(url)
    # driver.maximize_window()  # 窗口最大化
    # driver.implicitly_wait(5)  # 隐式等待5s
    get_captcha(driver)
    driver.implicitly_wait(3)
    captcha = recognize_captcha('captcha.png')
    print(captcha)
    time.sleep(10)


