import time

from DecryptLogin import login

'''自动发微博'''


class weiboSender():
    def __init__(self, username, password):
        self.nickname, self.uid, self.session = self.login(username, password)


    '''模拟登陆'''

    def login(self, username, password):
        client = login.Client()
        weibo = client.weibo(reload_history=True)
        infos_return, session = weibo.login(username, password, 'mobile')

        return infos_return.get('nick'), infos_return.get('uid'), session

    def logging(self,msg,tip='INFO'):
        print(f'[{time.strftime("%Y-%m-%d %H:%M%:%S")} {tip}]:{msg}')