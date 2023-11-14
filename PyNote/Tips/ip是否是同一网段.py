"""
1.将ip转为二进制,或子网掩码netmask转为二进制
# 取ip掩码长度的ip二进制值比较
2.将二进制的ip或二进制的子网掩码做与运算 & (都为1，则为1)
3.得到的结果比较
"""

# 方式 1
import ipaddress


def ip_bin(ip_address):
    # ip转为二进制
    new_ip = []
    # for i in ip_address.split('.'):
    #     new_i = bin((int(i)))[2:]
    #     if len(new_i) != 8:
    #         new_i = new_i + '0' * (8 - len(new_i))
    #     new_ip.append(new_i)
    # return ''.join(new_ip)
    ip_address = bin(int(ipaddress.IPv4Address(ip_address)))[2:]
    return ip_address


a_ip = "192.168.1.1"
b_ip = "192.168.1.3"
c_ip = "192.168.3.1"
net_mask = "255.255.255.0"
new_mask = ip_bin(net_mask)
length = new_mask.count('1') + 1
new_a = ip_bin(a_ip)
new_b = ip_bin(b_ip)
print(new_a, new_b, new_mask)
print(new_a[:length] == new_b[:length])

# 方式 2

ip = '192.168.1.1'
ip1 = '192.168.1.3'
ip2 = '192.168.2.1'

# 转为二进制

print("ip:", '.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
print("ip1:", '.'.join([bin(int(x) + 256)[3:] for x in ip1.split('.')]))
print("ip2:", [bin(int(x) + 256)[3:] for x in ip2.split(".")])
a = [bin(int(x) + 256)[3:] for x in ip.split('.')]
b = [bin(int(x) + 256)[3:] for x in ip1.split('.')]
c = [bin(int(x) + 256)[3:] for x in ip2.split('.')]
if a[:-1] == b[:-1]:
    print("同一网段")
if a[:-1] != c[:-1]:
    print("不同网段")
