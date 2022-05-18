# -*- coding:utf-8 -*-

dict_data={6:9,10:5,3:11,8:2,7:6}
"""1、对字典按键（key）进行排序 （默认由小到大）"""

d0=sorted(dict_data.keys())
print(d0)   #   输出结果[3, 6, 7, 8, 10]
d1=sorted(dict_data.items(),key=lambda x:x[0])
print(d1) #输出结果[(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]

"""2、对字典按值（value）进行排序 （默认由小到大）"""
d2=sorted(dict_data.items(),key=lambda x:x[1])
print(d2) #输出结果[('8', 2), ('10', 5), ('7', 6), ('6', 9), ('3', 11)]
d3=sorted(dict_data.items(),key=lambda x:x[1],reverse=True)
print(d3) #输出结果 [('3', 11), ('6', 9), ('7', 6), ('10', 5), ('8', 2)]

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

"""3.dict_data.items()#以列表返回可遍历的(键, 值) 元组数组。"""
for key, value in dict.items():
    print(key, value)

"""4.enumerate 枚举"""
for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

"""5.遍历两个或更多的序列，可以使用 zip() 组合"""
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print(f'What is your {q} It is {a}')
    #print('What is your {0}?  It is {1}.'.format(q, a))

"""6.sorted 函数的key= 参数没有调用str.uppper，而是把这个方法的引用传递给sorted 函数，这样在排序的时候，单词会被规范成统一格式"""
index = ["I","love","three","things","in","the","world","The","sun","the","moon"]
for word in sorted(index, key=str.upper):
    print(word)

