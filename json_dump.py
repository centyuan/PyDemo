# -*- coding:utf-8 -*-
import  json
#import os

a = {'name': 'wang', 'age': 29}
b = json.dumps(a)

#简单说就是dump需要一个类似于文件指针的参数（并不是真的指针，可称之为类文件对象），
#可以与文件操作结合，也就是说可以将dict转成str然后存入文件中；而dumps直接给的是str，
#也就是将字典转成str。
fp=open("testfile.txt", "w")
c= json.dump(a,fp)
fp.close()
print(b)
print(type(b))
print(c)