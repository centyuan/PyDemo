#   通过UDP的特性，如果一个端口没有开放，将会触发一个ICMP应答包，根据接收到的ICMP应答包，就可以反向推理出主机是存活的
import socket
import os

HOST = "192.168.9.99"
# os.name 用于查询操作系统类型
# posix:说明系统是Linux、Unix或Mac OS X
# nt:就是Windows系统
def main():
    if os.name =='nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    # socket.AF_INET 使用ipv4
    # socket.SOCK_RAW  原始套接字，可以处理ICMP、ARP等网络报文，其它的不行
    sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
    sniffer.bind((HOST,0))
    # 设置给定套接字选项的值。
    # 设置在捕获的数据包中包含IP头
    sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    # 如果在windows下 需要设置IOCTL以启用混杂模式
    if os.name =='nt':
        sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
    # 读取一个单独的数据包
    print(sniffer.recvfrom(65565))
    # 在windows下关闭混杂模式
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    main()