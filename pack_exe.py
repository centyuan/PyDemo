import cv2

# imgFilepath = "C:/Users/rainbow/Pictures/v2w.jpg"
imgFilepath = './image/v2w.jpg'
img = cv2.imread(imgFilepath)
cv2.imshow('img',img)
print("你好")
cv2.waitKey()

"""
Pyinstaller -F  -W  pack_exe.py  # -w 不打包工作台,有print语句则打包
Pyinstaller -F -w -i v2w.ico  pack_exe.py
"""



