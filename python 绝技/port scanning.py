import optparse
from socket import *
from threading import *
#使用semaphore 加锁，确保输出打印到屏幕顺序
screenLock = Semaphore(value=1)
def connscan(tgtHost,tgtPort):
    try:
        #socket.AF_INET 使用ipv4 默认
        #socket.SOCK_STERAM 流式socket,for Tcp 默认
        connSkt = socket(AF_INET,SOCK_STREAM)
        #失败抛出异常
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('Viiolent Python\r\n')
        results = connSkt.recv(100)
        screenLock.acquire() #print获取一个锁
        print("%d tcp open"%(tgtPort))
        print("[+]"+str(results))
        connSkt.close()
    except:
        screenLock.acquire()
        print("%d tcp closed"%(tgtPort))
    finally:
        screenLock.release() #释放锁
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost) #根据主机名（locaLhost 或www,baidu.com）返回IPv4
        #gethostbyaddr("127.0.0.1") ('DESKTOP-6EDJOQT', [], ['127.0.0.1'])
    except:
        print("Cannot resolve %s:Unknown host" % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("Scan Results for "+tgtName[0])
    except:
        print('Scan Results for'+tgtIp)
    #代表经过t秒后，如果还未下载成功，自动跳入下一次操作，此次下载失败。
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning port"+tgtPort)
        #connscan(tgtHost,int(tgtPort))
        #使用线程扫描
        t = Thread(target=connscan,args=(tgtHost,int(tgtPort)))
        t.start()
def main():
    parser = optparse.OptionParser("usage%prog"+"-H <target host> -p <target port>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s] separated by comma')
    options,args = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')
    if tgtHost==None | tgtHost[0]==None:
        print("You must specify a target host and port[s]")
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == "__main__":
    main()




