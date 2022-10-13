import cv2

# imgFilepath = "C:/Users/rainbow/Pictures/v2w.jpg"
imgFilepath = './image/v2w.jpg'
img = cv2.imread(imgFilepath)
cv2.imshow('img',img)
print("你好")
cv2.waitKey()

"""
Pyinstaller -F  -w  pack_exe.py  # -w 不打包工作台,有print语句则打包
Pyinstaller -F -w -i v 2w.ico  pack_exe.py
Pyintaller -D  -p  C:\Windows\System32\downlevel 
"""

"""

https://zhuanlan.zhihu.com/p/457972006
https://zhuanlan.zhihu.com/p/162866700
打包：freezeing
    PyInstaller ，py2exe，cx_Freeze,bbfreze,py2app...但是这些传统的库用来freezing一个PyQt程序还是有点难度的
    使用：fbs
    usage:
    fbs startproject
    fbs run
    fbs freeze
QT designer
    pyuic5 -o new.py new.ui

    D:\Program Files\Python36\python.exe -m PyQt5.uic.pyuic Weather.ui -o Weather.py
    python -m PyQt5.uic.pyuic  jiuyou_1.ui  -o jiuyou_1.py

"""

