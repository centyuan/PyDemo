import pyautogui as pag
import os
import time
try:
    while True:
        # 通过os.system直接调用操作系统功能
        # os.system('mstsc')远程连接
        # os.system("cmd")
        # os.system('cls') # 清屏
        # os.system("ping " + "www.baidu.com")
        # pag.moveTo(100, 300, duration=1) # 移动鼠标
        a = pag.size() # 获取屏幕分辨率
        a = '%4d,%4d'%pag.position()  # 获取鼠标坐标
        pag.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0) # 鼠标单击
        pag.typewrite(message='567528 I love three things',interval=0.5)
        pag.typewrite(message="原来入职")  #不能处理中文
        print(a)
except Exception as e:
    print(e)
"""
pag.doubleClick(10, 10)  # 指定位置，双击左键
pag.rightClick(10, 10)  # 指定位置，双击右键
pag.middleClick(10, 10)  # 指定位置，双击中键
pyautogui.mouseDown()   # 鼠标按下
pyautogui.mouseUp()    # 鼠标释放
pyautogui.scroll(300)  # 向下滚动300个单位
pyautogui.keyDown('shift')    # 按下shift
pyautogui.press('4')    # 按下 4
pyautogui.keyUp('shift')   # 释放 shift
pyautogui.typewrite('$*……%……￥', 0.5)  #  缓慢输出
pyautogui.hotkey('ctrl','c') 快捷键
im = pyautogui.screenshot() # 返回屏幕的截图，是一个Pillow的image对象
im.save('屏幕截图.png')
"""