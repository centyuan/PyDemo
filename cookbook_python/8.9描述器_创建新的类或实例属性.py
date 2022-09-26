"""
你想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查
"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
            # 如果一个描述器被当做一个类变量来访问，那么instance参数被设置成None
            # 这个时候标准做法就是简单返回这个描述器本身
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


"""
一个描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类，分别
为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。这些方法接受一个实
例作为输入，之后相应的操作实例底层的字典。
"""


class Point:
    # 在类上定义，不能再实例上定义
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# p = Point(2, 3)
# print(p.x)
# p.x = 2
abc = Integer('name')
abc.name = '你好'
print(abc, abc.name)
