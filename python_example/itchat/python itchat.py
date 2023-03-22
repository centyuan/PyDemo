#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-5 下午4:58
import itchat
from itchat.content import *
# itchat.auto_login()#扫码登录1：get uuid of QR, download,scan the QR
# itchat.send("hello,filehelper",toUserName='filehelper')#给文件助手发送信息

# @itchat.msg_register(TEXT)
# def _(msg):
#     # equals to print(msg['FromUserName'])
#     print(msg.fromUserName)打印msg

#各类型消息的注册回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    #return msg.text #自动回复发给自己的文本信息
    print(msg)
    msg.user.send("%s:%s"%(msg.type,msg.text))
    #send(msg='Text,Messages',toUserName=)


@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):#文件下载
    msg.download(msg.filename)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):#好友添加
    msg.user.verify()
    msg.user.send("Nice to meet you!")

@itchat.msg_register(TEXT,isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

itchat.auto_login(True)#hotReload等于True退出程序后暂存登陆状态
#用户搜索
print(itchat.search_friends(name='WAS'))
print(itchat.search_friends(name='张文'))
#print(itchat.search_friends(wechatAccount='w243499070'))
print(itchat.search_friends(name='付黎静'))
print(itchat.search_friends())#获取自己的用户信息，返回自己的属性字典
itchat.run(True)