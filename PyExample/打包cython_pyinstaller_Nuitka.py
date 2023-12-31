"""
### 一:单文件加密 https://www.cnblogs.com/traditional/tag/Cython/
打包成.so,源代码保护
1.pip install cython
    安装python-devel和gcc: yum install python-devel && yum install gcc
                          apt-get install python-devel && apt-get install gcc

2.准备待编译文件 hello.py
def greet(msg:str):
    return "hello"+str

3.准备setup.py
from distutils.core import setup
from Cpython.Build import cythonize

if __name__ == "__main__":
    file_name =  "D:\Vscode_project\test_something\test.py"
    setup(ext_modules=cythonize([file_name],language_level=3))  # [file_name,file_nam2]多个文件

4.执行并生产.so
# build_ext 编译个c/c++扩展
# --inplace 忽略build-lib，将编译后的扩展放到源目录中，与纯Python模块放在一起
python setup.py build_ext --inplace

或手动从命令行编译,使用 /user/local/bin/cython将.py/.pyx编译成C/C++ or /usr/local/bin/cythonize将.py/.pyx编译成C/C++后在编译成.so
example: /usr/local/bin/cythonize -3 -i --directive=always_allow_keywords=true .

### 二:编译整个目录
py2so

### 三:Nuitka 打包成so或exe
1.安装 
    pip install Nuitka
    安装C++编译器 gcc/MinGW64 (vs2019)
2.python -m nuitka  --module program.py
参数说明:
    --standalone 打成一个独立的分发环境
    --follow-imports 把import的文件或模块一起打包、
    --nofollow-imports 不打包所有import
    --nofollow-import-to 指定包不打进去
    --include-package=bigauth 指定包名 
    --onefile 打包成一个文件
    --plugin-enable=qt-plugins qt插件
    --module 打包成一个.so文件
    --show-progress 展示过程
    --show-memory 显示内存
    --remove-output 生成模块或exe文件后删除生产目录

python -m nuitka --module bigauth --include-package=bigauth --remove-output 
### 四:pyintaller 打包成exe
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

exe打包总结：pyinstaller垃圾,Nuitka真香
"""



from distutils.core import setup
from Cython.Build import cythonize

if __name__ == "__main__":
    file_name = "D:\Vscode_project\test_something\test.py"
    setup(ext_modules=cythonize([file_name]))

# python setup.py build_ext --inplace


### 五:setuptools打包(distutils)并上传到pypi
"""
项目打包发布总结:
python包分发:源码包/二进制包
源码包: .zip/.tar.gz
二进制包: egg/wheel

distutils是标准库
setuptools是distutils增强版

    1.确定项目结构
    2.编写setup.py(打包相关信息)
      LICENSE:可以通过github创建项目的时候选择,选择"MIT License" 后面需要添加对应的License版本
      README.md:项目的介绍
      setup.py: 打包时用到的元数据信息
      project_name: 项目主要的代码目录
    3.python3 setup.py sdist bdist_wheel     
      python setup.py sdist --formats=gztar,zip  # 源码包
      python setup.py bdist_wininst              # 打包成exe
      python setup.py bdist                      # 多种格式 
    4.同目录下产生dist目录(包括.whl和tar.gz源码包)
    5.twine check dist/*                         # twine是上传包到pypi的主要工具  
    6.twine uplaod dist/*                        # 上传
    7.安装 python setup.py install  # pip instal xxx.wheel    

"""
# cython教程
# https://www.cnblogs.com/traditional/tag/Cython/
# https://www.bookstack.cn/read/cython-doc-zh/docs-3.md