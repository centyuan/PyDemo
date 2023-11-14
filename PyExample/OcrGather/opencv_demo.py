import os
import time

import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'D:\softinstall\Tesseract-OCR\tesseract.exe'

def interference_line(img):
    """
    干扰线降噪
    :param img:
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



def clear_border(img):
    h, w = img.shape[:2]
    for y in range(0, 2):
        for x in range(0, h):
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if y < 2 or x > h - 2:
                img[x, y] = 255
    return img


def image_conprove(path):
    rgb_img = cv2.imread(path)
    # print(rgb_img.shape)
    # print(rgb_img[0,0])    # 像素(0,0)的值RGB [101 104 135]
    # print(rgb_img[0,0,2])  # 135
    # 1.调整大小
    h, w = rgb_img.shape[:2]
    img1 = cv2.resize(rgb_img, (int(h * 2), int(w * 2)))
    # cv2.imshow('img1',img1)
    # print('图片大小:',rgb_img.shape)

    # 2.灰度化，二值化
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('img2',img2)
    ret, img3 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('img3',img3)
    # ret, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # ret, img = cv2.threshold(gray, 185, 255, cv2.THRESH_BINARY_INV)
    # print(f'二值化设置的阈值：{ret}')

    # 3.去除边框
    img4 = clear_border(img3)
    # 4.去噪
    # blur = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
    img5 = interference_line(img4)
    # cv2.imshow('img4',img4)
    # cv2.imshow('img5',img5)
    # 5. 侵蚀和膨胀(允许字符边缘在共同背景下的腐蚀和膨胀，以扩大或增大尺寸（膨胀）或缩小（腐蚀）)
    # img6 = cv2.erode(img5, None, iterations=2)
    # img7 = cv2.dilate(img6, None, iterations=1)
    # cv2.imshow('img7', img7)
    # 6.逻辑运算  让背景为白色  字体为黑  便于识别
    # cv2.bitwise_not(img7, img7)
    return img5
    # cv2.imshow('img_last', img7)
    # cv2.waitKey(20000)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def laebel_filepaths():
    # file_path = os.path.dirname(__file__)+'/'+ 'resource'
    # file_path = os.path.dirname(__file__)+'/'+ 'resource'
    for filename in os.listdir('resource'):
        yield filename[:4], 'resource' +'/'+ filename


def main():
    total, true_num = 0, 0
    for label,file_path in laebel_filepaths():
        total +=1
        img = image_conprove(file_path)
        text = pytesseract.image_to_string(img)
        if text == label:
            true_num +=1
        print(text,label,text==label)
        time.sleep(5)
    print('识别率:{}'.format(true_num/total))




if __name__ == '__main__':
    main()