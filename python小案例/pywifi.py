#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-9 下午6:55


from pywifi import *
#获取是否连接网络
def Check_stat():

    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    print(ifaces.status())

    if ifaces.status() == 4:
        print('已连接无线')
    else:
        print("未连接")



if __name__ == "__main__":
    print(__name__)
    Check_stat()