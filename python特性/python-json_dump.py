#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-12 下午3:53
"""
dumps是将dict转化成str格式，loads是将str转化成dict格式。
json在python里面看成字符串
json.loads()将已编码的 JSON 字符串解码为 Python 对象
json.dumps()函数是将一个Python 对象编码成 JSON 字符串
"""
import json
#1: python object ->json.dumps()->json string
a = {'name': 'wang', 'age': 29,'gender':"男"}
b = {'city':{'country':'china','provider':'chendu'},'name':'zhongba','nums':20}
a1 = json.dumps(a,ensure_ascii=False)  #{"name": "wang", "age": 29, "gender": "\u7537"} 加个ensure_ascii=False
b1 = json.dumps(b)
print("json.dumps:",a1,type(a1))
print("json.dumps:",b1,type(b1))

#简单说就是dump需要一个类似于文件指针的参数（并不是真的指针，可称之为类文件对象），
#可以与文件操作结合，也就是说可以将dict转成str然后存入文件中；而dumps直接给的是str，也就是将字典转成str。

data = [{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json_data = json.dumps(data)
fp=open("testfile.txt", "w")
c= json.dump(a,fp)
fp.close()
print(c)

#2:json string ->json.loads python object
JsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(JsonData)
print('json.loads',text,type(text))

