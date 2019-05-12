#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-12 下午3:53
#dumps是将dict转化成str格式，loads是将str转化成dict格式。
#json.dumps()函数是将一个Python数据类型列表进行json格式的编码
import  json
a = {'name': 'wang', 'age': 29}
b = json.dumps(a)
print(b)
print(type(b))
#简单说就是dump需要一个类似于文件指针的参数（并不是真的指针，可称之为类文件对象），
#可以与文件操作结合，也就是说可以将dict转成str然后存入文件中；而dumps直接给的是str，也就是将字典转成str。
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

text = json.loads(jsonData)
print(text)
print(type(text))

fp=open("testfile.txt", "w")
c= json.dump(a,fp)
fp.close()

print(c)