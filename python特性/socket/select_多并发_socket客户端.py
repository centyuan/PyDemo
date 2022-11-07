import socket
import sys

msgs = [
    b'This is the message',
    b'It will be sent',
    b'in parts',
]
ip_port = ('127.0.0.1',8888)
# 创建500个Tcp/ip socket
sockets = [socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(500)]

print(f'connect to {ip_port} ')
for socket in sockets:
    socket.connect(ip_port)

for message in msgs:
    # 发送数据
    for socket in sockets:
        print(f'{socket.getsockname()}:sending {message}')
        socket.send(message)

    # read message
    for socket in sockets:
        data = socket.recv(1024)
        print(f'{socket.getsockname()} recived {data}')
        if not data:
            print(sys.stderr,'closing socket',socket.getsockname())
