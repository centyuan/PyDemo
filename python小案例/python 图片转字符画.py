#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-5 上午10:55
from PIL import Image
import argparse  #处理命令行参数

#创建命令行参数处理ArgumentParser实例
parser=argparse.ArgumentParser()
#定义输入文件,输出文件,输出字符画的宽高
parser.add_argument('file') #输入文件
parser.add_argument('-o','--output') #输出文件
parser.add_argument('--width',type=int,default=80) #输出字符高
parser.add_argument('--height',type=int,default=80)
#解析并获取参数
args=parser.parse_args()
#图片路径
IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output
#字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
print('-----------------------------')

def get_char(r,g,b,alpha=256):
    #判断alpha值,为0,表示图片该位置空白
    if not alpha:
        return ' '
    #获取字符长度
    length=len(ascii_char)
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    #处理
    unit=(256.0+1)/length
    #返回灰度值对应的字符
    return  ascii_char[int(gray/unit)]


if __name__=='__main__':
    #打开并调整图片宽高
    im=Image.open(IMG)
    #Image.NEAREST表示输出低质量的图片。
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt='' #输出字符串
    #遍历图片的每一行
    for i in range(HEIGHT):
        #遍历该行中的每一列
        for j in range(WIDTH):
            #im.getpixel((j,i)) 获取(j,i)位置的像素值
            txt +=get_char(*im.getpixel((j,i)))
        #遍历完每一行增加一个换行符
        txt +='\n'
    print(txt)
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
