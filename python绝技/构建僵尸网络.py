import optparse
from pexpect import pxssh
import  pysnooper
#Windows目前不支持pxssh.
"""
from pexpect import ExceptionPexpect, TIMEOUT, EOF, spawn
ImportError: cannot import name 'spawn'

"""
class Client():
    def __init__(self,host,user,password):
        self.host =host
        self.user =user
        self.password = password
        self.session = self.connect()
    @pysnooper.snoop()
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')
    def send_command(self,cmd):
        self.session.sendline(cmd)
        print(self.session.prompt())
        return self.session.before

if __name__ == '__main__':
    botNet =[]
    botNet.extend((Client('8.214.28.191','root','root'),Client('8.214.28.191','root','root')))
    for it in botNet:
        it.send_command('uname -v')
