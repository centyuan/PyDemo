"""
FTP服务允许用户基于一个tcp来传输文件，一般用户使用用户名和密码登录FTP服务器
一些FTP服务器提供匿名登录的能力(匿名FTP访问有助于网站访问软件更新)
"""
import ftplib


# 1.匿名登录扫描
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@yourc.com')  # 用户名：anonymous,密码：邮箱地址
        print("\n[*]" + str(hostname) + "FTP匿名登录successded")
        ftp.quit()
        return True
    except Exception as e:
        print("\n[*]" + str(hostname) + "FTP匿名登录failed")
        return False


# 2.暴力破解FTP口令
def bruteLgin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print("Trying:" + username + "/" + password)
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        print("FTP登录successded" + username + "/" + password)
        ftp.quit()
        return (username, password)
    except Exception as e:
        pass
    print("could not brute force FTP credentials")
    return (None, None)



# 3. FTP服务器上搜索web服务（搜索是否有index.html)
def returnDefault(ftp):
    try:
        dirlist = ftp.nlst()  # 获取目录下的文件
        """
        ftp.pwd() #返回当前所在位置
        ftp.mkd(pathname) #新建远程目录
        ftp.dir() #显示目录下文件信息
        ftp.rmd(dirname) #删除远程目录
        ftp.delete(filename) #删除远程文件
        """
    except Exception as e:
        dirlist = []
        print("不能列出目录内容")
        return
    retlist = []
    for fileName in dirlist:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print("发现文件"+fileName)
            retlist.append(fileName)
    return retlist

if __name__ == '__main__':
    host = '192.168.8.243'
    userName = ""
    passWord = ""
    ftp = ftplib.FTP(host)
    ftp.login(userName,passWord)
    returnDefault(ftp)
