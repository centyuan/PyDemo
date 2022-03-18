# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/1 21:21
"""
qusetion:python 定义自己的常量
在 Python 中，当我们对类的属性进行赋值时，会自动调用 object 类的 __setattr__() 函数.
该函数的定义如下：
object.__setatter__(self,name,value)
其中 object 类的 object.__dict__ 以字典的形式保存了所有已赋值的属性。
"""
import sys
class _const:
    # 自定义异常处理
    class ConstError(PermissionError):
        pass
    class ConstCaseError(ConstError):
        pass
    # 重写 __setattr__() 方法
    def __setattr__(self, name, value):
        if name in self.__dict__:  # 已包含该常量，不能二次赋值
            raise self.ConstError("Can't change const {0}".format(name))
        if not name.isupper():  # 所有的字母需要大写
            raise self.ConstCaseError("const name {0} is not all uppercase".format(name))
        self.__dict__[name] = value

# 将系统加载的模块列表中的 constant 替换为 _const() 实例
sys.modules[__name__] = _const()