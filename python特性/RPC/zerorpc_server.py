# zerorpc 不走http
# 基于tcp,速度快，并发高
import zerorpc

class caculate(object):
    def hello(self, name):
        return 'hello, {}'.format(name)

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return abs(x-y)

    def divide(self, x, y):
        return x/y


s = zerorpc.Server(caculate(),heartbeat=None)
s.bind('tcp://0.0.0.0:8000')
s.run()