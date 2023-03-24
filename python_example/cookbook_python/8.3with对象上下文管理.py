from socket import socket, AF_INET, SOCK_STREAM


# 1.单层with
class LazyConnection():
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
"""
编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行:
1.当出现 with语句的时候，对象的 __enter__() 方法被触发，它返回的值 (如果有的话) 会被赋值给as 声明的变量。
2.然后，with 语句块里面的代码开始执行。最后，__exit__() 方法被触发进行清理工作。
"""


# 2.多层with

class LazzyConnection_:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        # self.sock = None
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 默认最后一个，栈的形式
        self.connections.pop().close()


conn = LazzyConnection_(('www.python.org', 80))
with conn as s1:
    with conn as s2:
        pass
