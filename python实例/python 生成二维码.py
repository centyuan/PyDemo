"""
https://www.cnblogs.com/nthforsth/p/12290779.html

"""

from MyQR import myqr

# 1:myqr:可以自定义背景图片,不支持中文
# myqr.run(words='www.baidu.com',picture='ascii_dora.png')
# myqr.run(words='www.xj89.app/',picture='')
words = r"https://blog.csdn.net/unicorn_mitnick/"
version, level, qr_name = myqr.run(
    words,
    version=1,
    level="H",
    # picture=r'.ascii_dorapng',
    picture=r'60960684_p0.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=r"yuan.png",
)
# words:扫码显示的文字或者跳转的网址,str
# version：边长，int range(1,40)
# level：纠错登记，str，L,M,Q,H，默认为H
# picture：结合图片，str，二维码下显示的图片或动图
# colorized：颜色，bool，True为彩色，None为黑白
# contrast：对比度，float，调节图片的对比度
# brightness：亮度，float，调节图片的亮度，其余用法和取值与 contrast 相同
# save_name：存储文件名，str
# save_dir：存储位置，str，默认存储位置是当前工程目录

# 2:qrcode:自身不带显示自定义图片,支持显示中文
import qrcode

# 方式一:
img = qrcode.make('https://www.baidu.com')
# img = qrcode.make('欢迎来到我知乎')
# img.save()
img.show()

# 方式二:
# error_correction:二维码纠错功能
# box_size:每个格子像素
# border:边框包含的格子数
qr = qrcode.QRCode(version=10,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
qr.add_data('https://www.baidu.com')
qr.make(fit=True)
# 二维码的背景色和格子色
img = qr.make_image(fill_color='black', back_color='white');
img.save('test.png')
img.show()