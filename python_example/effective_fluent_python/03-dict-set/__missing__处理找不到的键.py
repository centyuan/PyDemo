"""
1:类继承了dict，然后这个继承类提供了__missing__ 方法，
2:在__getitem__ 碰到找不到的键的时候，Python 就会自动调用它，而不是抛出一个KeyError 异常。
3:__missing__ 方法只会被__getitem__ 调用（比如在表达式d[k] 中）。
4:__missing__ 方法对get 或者 __contains__（in 运算符会用到这个方法）这些方法的使用没有影响。
"""

# 以下例子处理键位str和int的混用，为了一致性:键全转为str,但使dict[13]也能查询
#1.继承dict
class StrKeyDict0(dict):
    def __missing__(self, key):
         # 找不到key，且key还是str,
       if isinstance(key,str):
           raise KeyError(key)
       return self(str(key))
    """get 方法把查找工作用self[key] 的形式委托给__getitem__， 这样在宣布查找失败之前，还能通过__missing__ 再给某个键一个机会。"""
    def get(self, key, default=None):
        try:
            return self[key]  # 交给__getitem__
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2','two'),('4','four'),(3,'three')])

# 继承UserDict
import collections
class StrKeyDict(collections.UserDict):
        def __missing__(self, key):
            if isinstance(key,str):
                raise KeyError(key)
            return self[str(key)]
        def __contains__(self, key):
            # data 的属性，是dict 的实例，这个属性实际上是UserDict 最终存储数据的地方
            return str(key) in self.data
        def __setitem__(self, key, value):
            # __setitem__ 会把所有的键都转换成字符串。
            self.data[str(key)] = value

