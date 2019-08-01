#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-22 下午6:53
post_data = {
    'mn': 'shanghu01',
    'mark': "20180927104432780",
    'name': "goods_1538016272",
    'money': "0.01",
    'type': "bankcard",
    'service': "0",
    'notify_url': "http://domain/notify",
    'return_url': "http://domain/returnUrl",
    'sign': "签名信息",

}
po_da = sorted(post_data.items(), key=lambda x: x[0])
print(po_da)
str=''
for one in po_da:
    str=str+one[0]+'='+one[1]+'&'

print(str)