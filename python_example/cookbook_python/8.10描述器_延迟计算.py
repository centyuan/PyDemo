"""
你想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。但
是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
"""


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('计算面积')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('计算周长')
        return 2 * math.pi * self.radius


#
c = Circle(4.0)
print(c.radius)
print(c.area, c.area)  # 仅计算一次，后存储
print(c.perimeter, c.perimeter)  # 仅计算一次,后存储
print(vars(c))  # vars() 函数返回对象object的属性和属性值的字典对象。
