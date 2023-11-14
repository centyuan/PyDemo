#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-9 上午11:42
import requests
import itchat

KEY='572129d518ad4132ba58f197552c3297'

def get_response(msg):
    apiUrl='http://www.tuling123.com/openapi/api'
    data={
        'key':KEY,
        'info':msg,#发出去的消息
        'userid':'wechat-robot',#
    }
    try:
        res=requests.post(apiUrl,data=data).json()
        print(res)
        return res.get['text']
    except:#捕获所有异常
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    default_reply='I received:'+msg['Text']
    reply=get_response(msg['Text'])
    print(reply,default_reply)
    # return reply or default_reply
    return default_reply
itchat.auto_login(True)
itchat.run()