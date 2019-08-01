#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-5 下午3:02
# import ipdb
from MyQR import myqr

myqr.run(words='www.baidu.com',picture='ascii_dora.png')
#myqr.run(words='www.xj89.app/',picture='')

# ipdb.set_trace()
# ipdb.set_trace(context=5)

words = r"https://blog.csdn.net/unicorn_mitnick/"
version, level, qr_name = myqr.run(
    words,
    version=1,
    level="H",
    picture=r'ascii_dora.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=r"yuan.png",
    )
#words:扫码显示的文字或者跳转的网址,str
#version：边长，int range(1,40)
#level：纠错登记，str，L,M,Q,H，默认为H
#picture：结合图片，str，二维码下显示的图片或动图
#colorized：颜色，bool，True为彩色，None为黑白
#contrast：对比度，float，调节图片的对比度
# brightness：亮度，float，调节图片的亮度，其余用法和取值与 contrast 相同
# save_name：存储文件名，str
# save_dir：存储位置，str，默认存储位置是当前工程目录