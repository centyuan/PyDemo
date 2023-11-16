import ipaddress

if __name__ == '__main__':
    net = ipaddress.ip_network('192.168.9.64/28')

    for a in net:
        print(a)