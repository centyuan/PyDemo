#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-12 下午3:53
#dumps是将dict转化成str格式，loads是将str转化成dict格式。
#json在python里面看成字符串
#json.loads()将已编码的 JSON 字符串解码为 Python 对象
#json.dumps()函数是将一个Python 对象编码成 JSON 字符串
import  json
#一:python对象变成json字符串
a = {'name': 'wang', 'age': 29}
s_temp4 = {'city':{'country':'china','provider':'chendu'},'name':'zhongba','nums':20}
b = json.dumps(a)
json_temp4=json.dumps(s_temp4)
print(b)
print(type(b))
print("json_temp4",json_temp4)
#简单说就是dump需要一个类似于文件指针的参数（并不是真的指针，可称之为类文件对象），
#可以与文件操作结合，也就是说可以将dict转成str然后存入文件中；而dumps直接给的是str，也就是将字典转成str。

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

fp=open("testfile.txt", "w")
c= json.dump(a,fp)
fp.close()
print(c)

#二:json字符串解析成python对象
JsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(JsonData)
print(text)
print(type(text))

response_data='{"mchid":10010, "data":"{ "paytype": 100, "out_trade_no": "20190610001"}"}'
a={response_data}
b=list(response_data)
print(a)
print(b)
print(json.loads('{"employees": [{ "firstName":"Bill" , "lastName":"Gates" },{ "firstName":"George" , "lastName":"Bush" },{ "firstName":"Thomas" , "lastName":"Carter" }]}'
))
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))

# s_temp5 = "{'city':{'country':'china','provider':'chendu'},'name':'zhongba','nums':20}"
# json_temp5=json.loads(s_temp5)
# print(json_temp5)
#python--- JsonPath从多层嵌套Json中解析所需要的值
dic =   {
        "error_code": 0,
        "name":"yuan",
        "stu_info": [
                {
                        "id": 2057,
                        "name": "xiaohei",
                        "sex": "nan",
                        "age": 29,
                        "addr": "beijing",
                        "grade": "tianxie",
                        "phone": "18712321234",
                        "gold": 100
                }
        ]
}
import jsonpath

s = jsonpath.jsonpath(dic,'$..name')   #不管有多少层，写两个.都能取到
print("s1",s) #['xiaohei'] 返回的是一个列表
s = jsonpath.jsonpath(dic,'$..hehe')   #当不存在hehe这个key时，返回false
print("s2",s)  #False