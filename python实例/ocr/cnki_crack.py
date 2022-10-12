import time
from PIL import Image
from selenium import webdriver
import pytesseract
import cv2 as cv


def get_captcha(driver,i):
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
    captcha.save(f'resource/captcha{i}'+'.png')  # 保存截取的验证码区域文件


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

def recognize_text2(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv.imshow('binary', binary)
    # 形态学操作  获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow('bin1', bin1)
    kernel = cv.getStructuringElement(cv.MORPH_OPEN, (2, 3))
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow('bin2', bin2)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(bin2, bin2)
    cv.imshow('binary-image', bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')

def recognize_text3(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化  设置阈值  自适应阈值的话 黄色的4会提取不出来
    ret, binary = cv.threshold(gray, 185, 255, cv.THRESH_BINARY_INV)
    print(f'二值化设置的阈值：{ret}')
    cv.imshow('binary', binary)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(binary, binary)
    cv.imshow('bg_image', binary)
    # 识别
    test_message = Image.fromarray(binary)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')



if __name__ == '__main__':
    url = 'https://my.cnki.net/Register/CommonRegister.aspx'
    driver = webdriver.Chrome(
        executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
    driver.get(url)
    for i in range(50):
        driver.get(url)
        driver.refresh()
        time.sleep(1)
        get_captcha(driver,i+1)
    # driver.implicitly_wait(3)
    # captcha_img = cv.imread(r'captcha.png')
    # captcha = recognize_captcha('captcha.png')
    # print(captcha)
    # recognize_text2(captcha_img)
    # recognize_text3(captcha_img)
    time.sleep(10)


