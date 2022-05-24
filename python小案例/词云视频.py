import requests
from bs4 import BeautifulSoup
import jieba
import cv2
import os
import numpy as np
import base64
from aip import AipBodyAnalysis
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import collections
from PIL import Image
import re
import random

#https://zhuanlan.zhihu.com/p/349955626

def download_video(video_url,save_path,video_name):
    '''
      youget 下载视频
      :param video_url:视频链接
      :param save_path: 保存路径
      :param video_name: 视频命名
      :return:
      '''
    # you-get -o 输出文件路径
    # you-get -O 输出文件名称
    # you-get -l [URL] 下载视频列表
    cmd = 'you-get -o{} -O {}'.format(save_path,video_name,video_url)
    # os.popen() 方法用于从一个命令打开一个管道。
    os.popen(r"D:\python_data\centyuan\cent30\Scripts\activate.bat",)
    res = os.popen(cmd,)
    #获取弹幕接口http://comment.bilibili.com/{cid}.xml # cid 为B站视频的cid 编号cid=419950348

def download_danmu():
    """
    弹幕下载并分词存储
    :return:
    """
    cid = "419950348"
    danmu_url = "http://comment.bilibili.com/{}.xml".format(cid)
    f = open("danmu.txt","w+",encoding="utf-8")
    res = requests.get(danmu_url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.txt,'lxml')
    items = soup.find_all('d') #找到所有d标签
    for item in items:
        text = item.text
        print(text)
        seg_list = jieba.cut(text,cut_all=True) #对字符串进行分词处理，方便后面制作词云图
        for j in seg_list:
            print(j)
            f.write(j)
            f.write('\n')
    f.close()

def seg(video_path,jpg_path,save_path,crop_path):
    Pic_path = r"D:\BaiduNetdiskDownload\python-demo\tempfile\picture"
    vc = cv2.VideoCapture(video_path)
    c=0
    if vc.isOpened():
        rval,frame = vc.read() #读取视频帧
    else:
        rval = False
    while rval:
        rval, frame = vc.read()  # 读取每一视频帧，并保存至图片中
        cv2.imwrite(os.path.join(Pic_path, '{}.jpg'.format(c)), frame)
        c += 1
        print('第 {} 张图片存放成功！'.format(c))
    #借助百度api进行人像分割
    APP_ID = "23633750"
    API_KEY = 'uqnHjMZfChbDHvPqWgjeZHCR'
    SECRET_KEY = '************************************'

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
    # 文件夹
    jpg_file = os.listdir(Pic_path)
    # 要保存的文件夹
    for i in jpg_file:
        open_file = os.path.join(jpg_path, i)
        save_file = os.path.join(save_path, i)
        if not os.path.exists(save_file):  # 文件不存在时，进行下步操作
            img = cv2.imread(open_file)  # 获取图像尺寸
            height, width, _ = img.shape
            if crop_path:  # 若Crop_path 不为 None,则不进行裁剪
                crop_file = os.path.join(crop_path, i)
                img = img[100:-1, 300:-400]  # 图片太大，对图像进行裁剪里面参数根据自己情况设定
                cv2.imwrite(crop_file, img)
                image = get_file_content(crop_file)
            else:

                image = get_file_content(open_file)

            res = client.bodySeg(image)  # 调用百度API 对人像进行分割
            labelmap = base64.b64decode(res['labelmap'])
            labelimg = np.frombuffer(labelmap, np.uint8)  # 转化为np数组 0-255
            labelimg = cv2.imdecode(labelimg, 1)
            labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
            img_new = np.where(labelimg == 1, 255, labelimg)  # 将 1 转化为 255
            cv2.imwrite(save_file, img_new)
            print(save_file, 'save successfully')






def main():
    #下载视频
    url = "https://www.bilibili.com/video/BV1ZY411j7DT?spm_id_from=333.1073.channel.secondary_floor_video.click"
    save_path = r"D:\BaiduNetdiskDownload\python-demo\tempfile"
    video_name = "ciyun_video"
    download_video(url,save_path,video_name)
    #下载弹幕
    download_danmu()

if __name__ == '__main__':
    main()