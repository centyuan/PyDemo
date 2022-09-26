# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/28 19:05
"""
property
将函数变为一个属性,不带()调用函数

"""


class test(object):
    def __init__(self):
        self.__num = 0

    def getNum(self):
        return self.__num

    def setNum(self, value):
        self.__num = value

    def delNum(self):
        del self.__num

    num = property(getNum, setNum, delNum)


class test_2(object):
    def __init__(self):
        self.__num = 0

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            # 类型检查
            raise TypeError('Expected a string')
        self.__num = value

    @num.deleter
    def num(self):
        del self.__num


print('test.num:', test.num)
test.num = 20
print('test.num', test.num)
print('test_2.num:', test_2.num)
test_2.num = 90
print('test_2.num:', test_2.num)

"""
hasattr():
hasattr()函数用于判断是否包含对应的属性
语法：
　　hasattr(object,name)
参数：
　　object--对象
　　name--字符串，属性名
返回值：
　　如果对象有该属性返回True，否则返回False

getattr():
描述：
　　getattr()函数用于返回一个对象属性值
语法：
　　getattr(object,name,default)
参数：
　　object--对象
　　name--字符串，对象属性
　　default--默认返回值，如果不提供该参数，在没有对于属性时，将触发AttributeError。
返回值：
　　返回对象属性值

setattr():
setattr()函数
描述：
　　setattr函数，用于设置属性值，该属性必须存在
语法：
　　setattr(object,name,value)
 参数：
　　object--对象
　　name--字符串，对象属性
　　value--属性值
返回值：
　　无

delattr():
描述：
　　delattr函数用于删除属性
　　delattr(x,'foobar)相当于del x.foobar
语法：
　　setattr(object,name)
参数：
　　object--对象
　　name--必须是对象的属性
返回值：
　　无


"""
