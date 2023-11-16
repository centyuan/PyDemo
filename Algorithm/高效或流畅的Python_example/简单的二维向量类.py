from math import hypot

"""
即便其他程序要使用这个类的这些方法，也不会直接调用它们，
一般由Python 的解释器会频繁地直接调用这些方法。
"""
class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #repr 对象的字符串表现形式
    """
    __repr__ 和__str__ 的区别在于，后者是在str() 函数被使用，
    或是在用print 函数打印 一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好
    如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择，因为如果一个对象没
    有__str__ 函数，而Python 又需要调用它的时候，解释器会用__repr__ 作为替代。
    """
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)
    #bool(x)背后调用x.__bool__(), 不存在该方法会调用 x.__len__(),len返回0 为False
    def __bool__(self):
        return bool(abs(self))
    # + 运算
    def __add__(self, other):
        x = self.x +other.x
        y = self.y +other.y
    # * 运算
    def __mul__(self, scalar):
        return Vector(self.x*scalar,self.y*scalar)
