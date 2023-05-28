"""
上下文管理器类
1.类实现了__enter__和__exit__,这个类的实例就是个上下文管理器,可以用with管理
2.通过装饰器,contextlib.contextmanager

__enter__:用于赋值给as后面的变量,
__exit__:清理正在使用的资源,且还包含了用于捕获异常
    exc_type:异常类型
    exc_value:异常值
    exc_tab:异常的位置(错误栈)
"""


class CTManager:
    def __enter__(self):
        print("__enter__被执行")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        @param exc_type:
        @param exc_val:
        @param exc_tb:
        """
        print("__exit__被执行")


with CTManager() as ct:
    print("显示上下文管理器")

