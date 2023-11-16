from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('get connection from:', self.client_address)  # client_address 客户端地址
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    print('开启服务')
    # TCPServer 是单线程的
    # serv = TCPServer(('127.0.0.1',9999),EchoHandler)
    # ThreadingTCPServer 创建线程没有限制
    serv = ThreadingTCPServer(('127.0.0.1', 9999), EchoHandler)
    serv.serve_forever()

# 客户端
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.send('Hello world'.encode())
print(s.recv(8192))
