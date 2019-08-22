#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-2 下午2:48
import  socket
import  time
import  threading

def tcplink(sock,addr):
    print("Accept new connection from %s:%s..."%addr)
    sock.send("Welcome!".encode())
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        send_data='hello,%s'%data
        sock.send(send_data.encode())
    sock.close()
    print("connection from %s:%s closed"%addr)

s=socket.socket() #创建socket对象
host=socket.gethostname() #获取本地主机名
port=12345         #设置端口
s.bind((host,port)) #绑定端口
s.listen(5)     #等待客户端连接
while True:
    c,addr=s.accept() #返回connect对象
    print("连接地址",addr)
    c.send("欢迎访问".encode())
    c.close()
    #可以使用多线程处理tcp连接
    # t=threading.Thread(target=tcplink,args=(c,addr))
    # t.start()
    # t.join()
    #由于 client 在服务器返回前主动断开连接会报BrokenPipeError: [Errno 32] Broken pipe错误



