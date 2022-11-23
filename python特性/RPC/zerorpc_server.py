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
        return abs(x - y)

    def divide(self, x, y):
        return x / y

    # 流响应类似生成器
    @zerorpc.stream
    def gen(self, start, end):
        for i in range(start, end):
            yield i


# s = zerorpc.Server(caculate(), heartbeat=None)
s = zerorpc.Server(caculate())
s.bind('tcp://127.0.0.1:8000')
s.run()
