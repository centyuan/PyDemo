import cv2 as cv
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
    # 边缘保留滤波  去噪
    dst = cv.pyrMeanShiftFiltering(image, sp=10, sr=150)
    # 灰度图像 COLOR_BGR2GRAY:灰度图
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 形态学操作   腐蚀  膨胀
    erode = cv.erode(binary, None, iterations=2)
    dilate = cv.dilate(erode, None, iterations=1)
    cv.imshow('dilate', dilate)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(dilate, dilate)
    cv.imshow('binary-image', dilate)
    # 识别
    test_message = Image.fromarray(dilate)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


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


src = cv.imread(r'../../captcha.png')
cv.imshow('input image', src)
recognize_text3(src)
# 参数<=0:
if cv.waitKey(0)==ord('A'):
    # 键盘敲击A时 销毁 imshow 展示的所有窗口
    cv.destroyAllWindows()
