"""
__slots__=['a']:
是python类的魔法属性,接受一个iterable对象作为属性
定以后,该类实例只能创建__slots__中声明的属性。
优点:
1.节省内存
没有__slots__,实例属性管理依赖__dict__字典
定义__slots__,实例属性管理依赖__slots__,实例不在拥有__dict__属性
__dict__字典在内存分配会预留较大的内存空间
__slots__则按照其中声明的属性分配定长内存
2.更快的访问速度
使用__slots__访问属性,节省了一次哈希的过程

"""


# 1.
class Test(object):
    __slots__ = ['a']


t = Test()
t.a = 1
Test.c = 2
print("属性a,c:", t.a, Test.c)
# t.b = 3  # AttributeError:'Test' object has no attribute 'b'
