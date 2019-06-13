#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-9 下午3:51
from math import  sqrt
from PIL import  Image
import itchat
import os

def getHeadImages():
    itchat.auto_login(hotReload=True)

    for friend in itchat.get_friends(update=True):
        print(friend['NickName'], friend['RemarkName'], friend['Sex'], friend['Province'], friend['Signature'])
        img = itchat.get_head_img(userName=friend["UserName"])
        image_path="/home/centyuan/PycharmProjects/py_test/image/HeadImages/"+friend['NickName']+"("+friend['RemarkName']+").jpg"
        #保存图片到本地
        try:
            with open(image_path,'wb') as f:
                f.write(img)
        except Exception as e:#Exception是万能的异常捕捉方法，可以捕捉到任何错误。
            print(repr(e)) #repr() 函数将对象转化为供解释器读取的形式。
    itchat.run()

def joinHeadImages():
    HeadImages_path="/home/centyuan/PycharmProjects/py_test/image/HeadImages/"
    pathList=[]
    for item in os.listdir(HeadImages_path):
        imaPath=os.path.join(HeadImages_path,item)
        pathList.append(imaPath)#得到每张图片path的列表
    total=len(pathList)#图片总数
    line=int(sqrt(total))#拼接图片的行数
    NewImage = Image.new('RGB', (128 * line, 128 * line))
    x = y = 0
    for item in pathList:
        try:
            img = Image.open(item)#打开图片，返回一个image对象
            img = img.resize((128, 128), Image.ANTIALIAS)#图像转换大小
            NewImage.paste(img, (x * 128, y * 128))#将img粘贴到NewImage的(x*128,y*128)
            x += 1
        except IOError:
            print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
            x -= 1
        if x == line:
            x = 0
            y += 1
        if (x + line * y) == line * line:
            break
    NewImage.save(HeadImages_path + "final.jpg")

if __name__=='__main__':
    joinHeadImages()


