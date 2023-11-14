# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/19 14:24

import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_host = ('127.0.0.1',12346)

sk.bind(ip_host)

while True:
    data = sk.recv(1024)
    print(data.decode())