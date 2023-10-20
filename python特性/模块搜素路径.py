"""
一:模块modules,任何以.py文件都可以作为模块,其他可作为module的文件类型还有so,pyo,pyc,dll,pyd
导入模块:
    1.import 模块名 [as 别名]:模块本身被导入,保存它原有的命名空间,所有用模块名.成员名访问函数或变量
    2.from 模块名 import [as 别名] 成员名:模块的函数/变量导入当前模块命名空间
模块搜索路径:
    导入一个模块时,Python解析器对模块位置的搜索顺序是：
    首先判断这个module是不是built-in即内建模块，如果是则引入内建模块，不是则搜索sys.path中的路径列表
    包含以下:
        1.当前目录
        2.PYTHONPATH中的每个目录。
        3.Python默认的安装目录
    模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
使用模块优势:
    1.有效避免命名空间的冲突
    2.较大程序分为多个文件,提升代码的可维护性和可重用性


二:包package(多个模块的集合),大型项目需要用到大量模块,可以用包package来管理这些模块,包含有__init__.py
    (__init__.py本身是个模块,模块名就是包的名,它的作用是将一个文件夹变为一个Python模块)
    包具有三个性质:1.实质上是一个文件夹,2.文件夹下一定包含__init__.py模块,3.本质依然是模块,可以装其他包
    通常__init__.py文件为空：一般会包含写初始化代码,我们在导入一个包时，实际上是导入了它的__init__.py文件,执行了这些代码,导入对应模块会执行对于模块。
    __all__是python中的一个重要变量,放在__init__模块中,用于指定此包package被import *时,那些模块会被import.
导入包：
    1.import 包名.[.模块名 [as 别名]]
    2.from 包名 import 模块名 [as 别名]
    3.from 包名.模块名 import 成员名 [as 别名]
总结:
    数据可以封装在容器里(list,tuple,str,dict)
    代码可以封装在function里
    function和数据可以封装在class里面
    上述三个可以打包在module里
    多个module可以打包在package里
    多个package可以打包在library里

三:库library,严格说python中没有库的概念
"""
import sys
import os

print(sys.path)

"""
step1:为待导入的模块创建module类的实例：模块对象(目前是空对象)将该module对象 插入sys.modules中
step2:将该module对象 插入sys.modules(字典类型)中；
step3:装载module的代码（如果需要，需先编译）；
step4:执行新的module中对应的代码。
"""
# 1.控制模块被全部导入的内容
__all__ = []  # 控制导出

# 2. 相对路径导入包中子模块
# from . import args_kwargs
# from ..B import bar

# 3.添加路径以便import
sys.path.append('path')
# sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__))),'src')
