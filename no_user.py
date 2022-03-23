# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/13 15:11

def dec(f):
    n = 3
    print('dec')
    def wrapper(*args, **kw):
        print('wrapper')
        return f(*args, **kw) * n
    return wrapper
@dec
def foo(n):
    print('foo')
    return n * 2

class Rect:

    def __init__(self,width,height):

        self.width = width

        self.height = height

    @property
    def area(self):

        return self.height* self.width

rect = Rect(10,20)
rect.area