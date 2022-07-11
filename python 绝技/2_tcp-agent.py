import socket
import sys
import threading

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])


# 类似 wireshark 以16进制和 可打印字符 形式打印内容
def hexdump(src,length=16,show=True):
    if isinstance(src,bytes):
        src = src.decode('utf8','ignore')
    results =list()
    for i in range(0,len(src),length):
        word = str(src[i:i+length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02x}' for c in word])
        hexwidth = length * 3
        results.append(f'{i:04X} {hexa:<{hexwidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results

# 从代理两端接收数据
def receive_from(connection):
    buffer = b''
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer +=data
    except Exception as e:
        pass
    return buffer

# 修改包
def request_handler(buffer):
    return buffer
def response_handler(buffer):
    return buffer

def proxy_handler(client_socket,remote_host,remote_port,receive_first):
    # 连接远程主机
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_socket.connect((remote_socket,remote_port))
    # 是否先从服务端接收一段数据
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer) # 打印内容 wireshark形式
        remote_buffer = response_handler(remote_buffer)
        if len(remote_buffer):
            print("[<==] 发送 %d bytes to 本地"%len(remote_buffer))
            client_socket.send(remote_buffer)
    while True:
        local_buffer = receive_from(client_socket)  # 从本地接收数据
        if len(local_buffer):
            line = "[==>]接收 %d bytes from localhost." % len(local_buffer)
            print(line)
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_host.send(local_buffer)
            print("[==> 发送 to remote ]")
        remote_buffer = receive_from(remote_socket)   # 从远程接收数据
        if len(remote_buffer):
            print("[<==] 接收 %d bytes from remote "%len(remote_buffer))
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] 发送 to localhost")
        # 异常处理
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print('[*] 没有数据,关闭连接')
            break

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind(local_host,local_port)  # 绑定本地ip端口
    except Exception as e:
        print("绑定异常 %r"%e)
        print("[!!] 失败监听%s:%d" % (local_host, local_port))
        print("[!!] 检测是否有其他连接或是否有权限.")
        sys.exit(0)
    print("[*] Listening on %s:%d" % (local_host, local_port))
    server.listen(5)  # 最大连接数5
    while True:
        client_socket,addr = server.accept()  # 返回connect对象
        line = ">接受连接进来 from %s:%d"%(addr[0],addr[1])
        print(line)
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,remote_port,receive_first))
        proxy_thread.start()

def main():
    if len(sys.argv[1:]) !=5:
        print("Useage ./proxy.py [localhost] [localport]", end="")
        print("[remotehost] [remoteport] [receive_first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)
    local_host = sys.argv[1]
    local_port = sys.argv[2]
    remote_host = sys.argv[3]
    remote_port = sys.argv[4]
    receive_first = sys.argv[5]
    # sys.argv[0] 为文件名
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)

if __name__ == '__main__':
    main()



