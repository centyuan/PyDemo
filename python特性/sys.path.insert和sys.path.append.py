#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-29 上午11:23
import sys
#sys.path模块是动态的修改系统路径

"""
sys.path是个列表
python程序中使用 import XXX 时，python解析器会在当前目录、已安装和第三方模块中搜索 xxx，如果都搜索不到就会报错。
使用sys.path.append()方法可以临时添加搜索路径，方便更简洁的import其他包和模块。但我们不喜欢维护一个永久性的大目录，
因为其他所有的Python脚本和应用程序导入模块的时候性能都会被拖累。在该路径中添加了一个"目录"，
当然前提是此目录存在而且此前不在sys.path中。
这种方法导入的路径会在python程序退出后失效。
sys.path是个列表，所以在末尾添加目录是很容易的，用sys.path.append就行了。
当这个append执行完之后，新目录即时起效，以后的每次import操作都可能会检查这个目录。
如同解决方案所示，可以选择用sys.path.insert(0,…)，这样新添加的目录会优先于其他目录被import检查。

"""