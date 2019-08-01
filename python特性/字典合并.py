#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-30 下午3:32

#一:dict(d1.items()+d2.items()) 现在不支持了
d1={'usr':'root','pwd':'123456'}
d2={'ip':'127.0.0.1','port':'8080'}
#print(dict(d1.items()+d2.items()))

#二:dict.update方法
d3={}
d3.update(d1)
d3.update(d2)
print('二:',d3)

#三:字典 dict(d1,**d2)
d3=dict(d1,**d2)
print('三:',d3)

#四:字典的常规处理
for k,v in d1.items():
    d3[k] = v
for k,v in d2.items():
    d3[k] = v
print('四:',d3)