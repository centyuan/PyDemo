import time
from pynput import  mouse,keyboard

time.sleep(5)

m_mouse = mouse.Controller() #创建鼠标
m_keyboard = keyboard.Controller() #创建键盘
m_mouse.position = (850,799) #移动鼠标
m_mouse.click =(mouse.Button.left) #点击左键

while(True):
    m_keyboard.type("浮世三千，吾爱有三") #打字
    m_keyboard.press(keyboard.Key.enter) #按enter
    m_keyboard.release(keyboard.Key.enter) #松开
    time.sleep(0.2)

