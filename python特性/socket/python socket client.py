#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-3 上午10:15
# 导入 socket、sys 模块
import socket
import sys

""""
socket.AF_INET 使用ipv4 默认
socket.AF_INET6 使用ipv6 
socket.AF_UNIX 只能用于单一的Unix系统进程间通信
socket.SOCK_STERAM 流式socket,for Tcp 默认
socket.SOCK_DGRAM  数据报式socket for udp
socket.SOCK_RAW   原始套接字
socket.SOCK_RDM   可靠的UDP形式
socket.SEQPACKET  可靠的连续数据包服务
"""
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
# host = socket.gethostname()
host = '127.0.0.1'
# 设置端口号
port = 12345
# 连接服务，指定主机和端口
s.connect((host, port))
# 接收小于 1024 字节的数据
msg = s.recv(1024)
print(msg.decode('utf-8'))
while True:
    data = s.recv(1024)
    print(data.decode())
    msg_input = input('请输入要发送的消息:')
    s.send(msg_input.encode())
    if msg_input == b'exit':
        break
s.close()
