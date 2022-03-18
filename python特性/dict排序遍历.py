# -*- coding:utf-8 -*-

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
po_da = sorted(post_data.items(), key=lambda x: x[0])
print('psot_data:',po_da)

#初始化字典
dict_data={6:9,10:5,3:11,8:2,7:6}
#1、对字典按键（key）进行排序
#对字典按键（key）进行排序（默认由小到大）
test_data_0=sorted(dict_data.keys())
print(test_data_0) #输出结果[3, 6, 7, 8, 10]

test_data_1=sorted(dict_data.items(),key=lambda x:x[0])
print(test_data_1) #输出结果[(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]

#2、对字典按值（value）进行排序
#对字典按值（value）进行排序（默认由小到大）
test_data_2=sorted(dict_data.items(),key=lambda x:x[1])
print(test_data_2) #输出结果[('8', 2), ('10', 5), ('7', 6), ('6', 9), ('3', 11)]

test_data_3=sorted(dict_data.items(),key=lambda x:x[1],reverse=True)
print(test_data_3) #输出结果 [('3', 11), ('6', 9), ('7', 6), ('10', 5), ('8', 2)]

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % dict.items())
#dict_data.items()#以列表返回可遍历的(键, 值) 元组数组。
# 遍历字典列表
for key, value in dict.items():
    print(key, value)
# enumerate 枚举
for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
#遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print(f'What is your {q} It is {a}')
    #print('What is your {0}?  It is {1}.'.format(q, a))