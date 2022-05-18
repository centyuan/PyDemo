#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-30 下午3:32

d1={'usr':'root','pwd':'123456'}
d2={'ip':'127.0.0.1','port':'8080'}

#y一:dict.update方法
d3={}
d3.update(d1)
d3.update(d2)
print('dict.update:',d3)
#二 python3.5后
d = {**d1,**d2}
print(d)

#三:字典 dict(d1,**d2)
d3=dict(d1,**d2)
print('dict():',d3)

#四:字典的常规处理
for k,v in d1.items():
    d3[k] = v
for k,v in d2.items():
    d3[k] = v
print('四:',d3)

response_dict={'data': {'trade_no': '3678497566409883648', 'total_fee': '100.00', 'paytype': 103, 'payurl': 'http://tpay.szspzc.xyz/gopay/index?trade_no=3678497566409883648', 'out_trade_no': '201906100156', 'mark': '13218', 'createdate': '2019-08-04 17:16:04'}, 'error': 0, 'msg': '', 'serverTime': 1564910160, 'sign': '93053fee773ba517131d5029eabdaa47'}
print(response_dict['data']['trade_no'])
print(response_dict['error'])
print(response_dict["data"]["total_fee"])