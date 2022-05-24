# 1.原始
def true_ip(address):
    try:
        ip_str = address[:-3]
        if len(ip_str) !=4:
            raise Exception("格式不正确,请输入正确格式")
        a,b,c,d = ip_str
        a, b, c, d = int(a), int(b), int(c), int(d)
        if 255>= max(a,b,c,d) and 0<=min(a,b,c,d):
            return True
        else:
            raise Exception("非法ip  {}".format(".".join(address)))

    except Exception as e:
        return False,str(e)

# 2. IPy
from IPy import  IP

def is_ip(address):
    try:
        IP(address)
        print(True)
        return True
    except Exception as e:
        print(False)
        print(str(e))
        return False,str(e)
is_ip("555555")
address = "192.168.1.0/16"
ip = str(address)[:-3]
print(ip)
