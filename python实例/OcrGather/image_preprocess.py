import re
import time
import cv2
import numpy as np
import os
import pytesseract
from PIL import Image


# 提升识别的准确率
# 1.利用jTessBoxEditor进行字库训练
# 2.对图片进行预处理(官方说明:https://tesseract-ocr.github.io/tessdoc/ImproveQuality
"""
图片预处理常用方法
1.放大图片
2.图像灰度化
3.二值化
4.去除边框
5.降噪
...
"""
# https://blog.csdn.net/weixin_43881394/article/details/108293799
# https://blog.csdn.net/qq_42103091/article/details/107667926

def GrayImage(img):
    """
    功能对图像进行灰度化
    """
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #转化为灰度图
    return img

def ResizeImage(img,ratio):
    """
    功能：重置图片大小
    image_path：图片路径
    ratio：图片的缩放比例
    """
    h, w = img.shape[:2]
    nw,nh = int(ratio*w),int(ratio*h)
    img = cv2.resize(img,(nw,nh))
    return img

def Binarisation(img):
    """
    将图片二值化
    img：待处理的图像
    """
    _,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    return img

def ClearBorder(img):
    """
    功能：去除边框
    """
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if x < 2 or x > h -2:
                img[x, y] = 255
    return img

def interference_line(img):
    """
    功能：线降噪
    """
    h, w = img.shape[:2]
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            if np.all(img[x, y - 1] > 245):
                count = count + 1
            if np.all(img[x, y + 1] > 245):
                count = count + 1
            if np.all(img[x - 1, y] > 245):
                count = count + 1
            if np.all(img[x + 1, y] > 245):
                count = count + 1
            if count > 2:
                img[x, y] = 255
    return img


def FilePaths(file_path=''):
    """
    功能：获取图片路径名及真实标签
    """
    # file_path = os.path.join(os.path.dirname(__file__),'resource')
    for filename in os.listdir('resource'):
        # yield filename[:-4],file_path + filename
        yield filename[:4],'resource/' + filename

def Recognition():
    total,true_num = 0,0
    for tab,file_path in FilePaths():
        total += 1
        mark = False
        img = cv2.imread(file_path)
        img = ResizeImage(img,2)
        img = GrayImage(img)
        img = Binarisation(img)
        img = ClearBorder(img)
        img = interference_line(img)
        text = pytesseract.image_to_string(img)
        new_text = re.findall(r'(\w+)', text)[0] if re.findall(r'(\w+)', text) else None
        if str(new_text) == str(tab):
            mark = True
            true_num += 1
        # for i in range(4):
        #     if new_text[0] != tab[0]:
        #         mark = False

        print('识别:',new_text,tab,mark)
        time.sleep(1)
    print("识别准确率为{}".format(true_num/total))

def Recognitino1(path,lable,total,true_num):

    img = cv2.imread(path)
    img = ResizeImage(img, 2)
    img = GrayImage(img)
    img = Binarisation(img)
    img = ClearBorder(img)
    img = interference_line(img)
    text = pytesseract.image_to_string(img, lang='eng')
    if str(text) == str(lable):
        print('true_num+1')
        true_num+=1
    total +=1
    print(f'识别结果{lable}:{text}',true_num,total)




def recognize_text0(file):
    # PIL预处理简单处理
    gray = Image.open(file).convert('L')  # 灰度化
    # gray.show()
    w, h = gray.size
    data = gray.load()  # 数值化,分配内存加载二位点阵数据
    for i in range(w):
        for j in range(h):  # 点阵里面的值，以128为界,置为0或255,即黑非百
            if data[i, j] < 128:
                data[i, j] = 0
            else:
                data[i, j] = 255

    text = pytesseract.image_to_string(gray)
    print(f'识别结果：{text}')


def recognize_text1(image):
    # 1.边缘保留滤波  去噪
    dst = cv2.pyrMeanShiftFiltering(image, sp=10, sr=150)
    # 2.灰度图像 COLOR_BGR2GRAY:灰度图
    gray = cv2.cv2tColor(dst, cv2.COLOR_BGR2GRAY)
    # 3.二值化
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 4.形态学操作   腐蚀  膨胀
    erode = cv2.erode(binary, None, iterations=2)
    dilate = cv2.dilate(erode, None, iterations=1)
    cv2.imshow('dilate', dilate)
    # 5.逻辑运算  让背景为白色  字体为黑  便于识别
    cv2.bitwise_not(dilate, dilate)
    cv2.imshow('binary-image', dilate)
    # 识别
    test_message = Image.fromarray(dilate)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


def recognize_text2(image):
    # 1.边缘保留滤波  去噪
    blur = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
    cv2.imshow('dst', blur)
    # 2.灰度图像
    gray = cv2.cv2tColor(blur, cv2.COLOR_BGR2GRAY)
    # 3.二值化
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv2.imshow('binary', binary)
    # 4.形态学操作  获取结构元素  开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 2))
    bin1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow('bin1', bin1)
    kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (2, 3))
    bin2 = cv2.morphologyEx(bin1, cv2.MORPH_OPEN, kernel)
    cv2.imshow('bin2', bin2)
    # 5.逻辑运算  让背景为白色  字体为黑  便于识别
    cv2.bitwise_not(bin2, bin2)
    cv2.imshow('binary-image', bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


def recognize_text3(image):
    # 1.边缘保留滤波  去噪
    blur = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
    # cv2.imshow('dst', blur)
    # 2.灰度图像
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # 3.二值化  设置阈值  自适应阈值的话 黄色的4会提取不出来
    ret, binary = cv2.threshold(gray, 185, 255, cv2.THRESH_BINARY_INV)
    # print(f'二值化设置的阈值：{ret}')
    # cv2.imshow('binary', binary)
    # 4.逻辑运算  让背景为白色  字体为黑  便于识别
    cv2.bitwise_not(binary, binary)
    # cv2.imshow('bg_image', binary)
    # 识别
    test_message = Image.fromarray(binary)
    text = pytesseract.image_to_string(test_message,None)
    new_text = re.findall(r'(\w+)',text)[0] if re.findall(r'(\w+)',text) else None
    print(f'识别结果：{new_text}')



if __name__ == "__main__":

    Recognition()