#1. lazy加载
"""
lazy:延迟加载,在需要的时候加载，而不是一开始就加载
优点:暂时不需要的包不导入减少了启动时间
缺点:开始发现不了导包错误
三种方式:
1.import放到函数内部
2.__getattr__
"""

#2.__import__
# 用于动态导入模块,主要用于反射或延迟加载模块,A = __import__(A)相当于import A
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None
    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
            return getattr(self.module, name)

#3. importlib
# 用户动态导入模块/切换模块
import importlib
importlib.import_module("os.path")


#4.getattr, __getattr__, __getattribute__和__get__区别
"""
getattr:为内置函数,获取对象的属性和方法,还有hasattr
__getattr__:访问对象属性不存在,会被调用
__getattribute__:访问对象属性会被调用
__get__：描述符方法

"""