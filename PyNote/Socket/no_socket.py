# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/19 14:30

import socketserver


# socketserver 实现非阻塞

class MyServer(socketserver.BaseRequestHandler):
    # 执行顺序 setup->handle->finish
    def setup(self):
        pass

    # 执行报错会跳过该方法
    def handle(self):
        # 定义连接变量
        conn = self.request
        # 发送消息定义
        msg = "hello world"
        conn.send(msg.encode())
        while True:
            # 接收客户端消息
            data = conn.recv(1024)
            print(data.decode())
            if data == b'exit':
                break
            conn.send(data)
        conn.close()

    def finish(self):
        pass


if __name__ == "__main__":
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 12346), MyServer)
    # 开启多线程，等待连接
    server.serve_forever()
