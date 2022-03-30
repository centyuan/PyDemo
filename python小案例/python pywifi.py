
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-9 下午6:55

#MOWIFI_2.4G_60AD:pq123789
import pywifi
import sys
#获取是否连接网络
def Check_stat():

    wifi = pywifi.PyWiFi()
    #获取无线网卡
    ifaces = wifi.interfaces()[0]

    print('status:',ifaces.status()) #无线网卡状态
    print('name',ifaces.name()) #无线网卡名称

    if ifaces.status() == 4:
        print('已连接无线')
    else:
        print("未连接")



if __name__ == "__main__":
    #sys.path是python的搜索模块的路径集，是一个list
    #Python解释器会自动将当前工作目录添加到sys.path
    print(sys.path )
    print(__name__)
    Check_stat()