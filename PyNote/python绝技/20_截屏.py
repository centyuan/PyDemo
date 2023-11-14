import base64
import win32api
import win32con
import win32gui
import win32ui

def get_dimensions():
    # 获得所有显示屏的像素尺寸
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width,height,left,top)

def screenshot(name="screenshot"):
    # 获得桌面窗口的句柄
    hdesktop = win32gui.GetDesktopWindow()
    width,height,left,top = get_dimensions()
    # 创建设备描述表
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    # 创建基于内存的设备描述表
    mem_dc = img_dc.CreateCompatibleDC()
    # 创建位图对象
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc,width,height)
    mem_dc.SelectObject(screenshot)
    # 复制屏幕到我们的内存设备描述表中
    mem_dc.BitBlt((0,0),(width,height),img_dc,(left,top),win32con.SRCCOPY)
    # 将位图保存到文件
    screenshot.SaveBitmapFile(mem_dc,f"{name}.bmp")
    # 释放对象
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def run():
    screenshot()
    with open("screenshot.bmp") as f:
        img = f.read()
    return img

if __name__ == "__main__":
    screenshot()
