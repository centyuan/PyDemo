from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn


# 1.单线程
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', '/RPC3')


# 多线程

class ThreaXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass



class JiSuan:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return abs(x - y)

    def divide(self, x, y):
        return x / y


def add_mu(x, y):
    return x + y


# 单线程
# with SimpleXMLRPCServer(('127.0.0.1', 8000), requestHandler=RequestHandler) as server:
# 多线程
with ThreaXMLRPCServer(('127.0.0.1', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    # 注册函数
    server.register_function(pow)
    # server.register_function(add_mu,'add_')
    # @server.register_function(name='add1')
    # def adder_function(x, y):
    #     return x + y + 1
    #
    #
    # @server.register_function()
    # def mul(x, y):
    #     return x * y

    server.register_instance(JiSuan())
    server.serve_forever()
