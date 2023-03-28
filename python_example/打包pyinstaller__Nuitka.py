"""
# 1.pyinstaller
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

# 2.Nuitka 打包
"""
