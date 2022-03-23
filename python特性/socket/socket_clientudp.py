# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/19 14:27

import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #DRRAM为udp

ip_host = ('127.0.0.1',12346)
while True:
    msg_input = input('请输入发送的消息')

    if msg_input == 'exit':
        break
    sk.sendto(msg_input.encode(),ip_host)
sk.close()