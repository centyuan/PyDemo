"""
3种窗口:
QMainWindow:包含菜单栏,工具栏,状态栏,标题栏,最常见的窗口形式
QDialog:是对话窗口的基类,没有菜单栏，工具栏,状态栏
QWidget: 不确定窗口的用途

参考资料:https://zhuanlan.zhihu.com/p/457972006
安装:https://zhuanlan.zhihu.com/p/162866700

Pyinstaller -F  -w  pack_exe.py  # -w 不打包工作台,有print语句则打包
Pyinstaller -F -w -i v 2w.ico  pack_exe.py
Pyintaller -D  -p  C:\Windows\System32\downlevel


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