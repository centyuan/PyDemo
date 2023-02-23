"""
上下文管理器类
类实现了__enter__和__exit__,这个类的实例就是个上下文管理器,可以用with管理

"""


class CTManager:
    def __enter__(self):
        print("__enter__被执行")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__被执行")


with CTManager() as ct:
    print("显示上下文管理器")

