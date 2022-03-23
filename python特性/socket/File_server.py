# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/19 14:47

import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)

sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept() #连接

    while True:
        #一直用当前连接接收数据
        with open('recieved_file','ab') as f:
            data = conn.recv(1024)
            if data ==b'quit':
                break
            f.write(data)
        #发送接收完成标志 (q:解决tcp粘包问题
        conn.send('success'.encode())
sk.close() #关闭连接
