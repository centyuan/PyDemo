#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-3 上午10:15
import socket

s=socket.socket() #创建socket对象
host=socket.gethostname()
port=12345
s.connect((host,port))
for data in ['Muchal','Tracy','Sarach']:
    s.send(data.encode())
    print(s.recv(1024))
s.send('exit'.encode())

s.close()
