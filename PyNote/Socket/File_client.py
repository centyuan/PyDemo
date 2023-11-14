# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/19 14:47
import socket


file_send = socket.socket()
#连接的ip port

ip_port = ('127.0.0.1',9999)
file_send.connect(ip_port)

with open('no_socket.py','rb') as f:
    #按每一段分割文件
    for i in f:
        #数据上传
        file_send.send(i)
        #等待接收完成标志
        data_sign = file_send.recv(1024)
        if data_sign !=b'success':
            break

#给服务器发送结束信号
file_send.send('quit'.encode())