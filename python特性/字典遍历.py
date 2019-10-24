# -*- coding:utf-8 -*-

a={'a': '1', 'b': '2', 'c': '3'}
a_num=a.items()
print(a.items(),type(a.items()))
#1遍历key值
for key in a:
    print("1遍历key值方式一",key+':'+a[key])
for key in a.keys():
    print("1遍历key值方式二",key + ':' + a[key])
#2遍历value的值
for value in a.values():
    print("2遍历value的值",key + ':' + value)
#3遍历字典项
for kv in a.items():
    print('3遍历字典项:',kv)
#4遍历字典健值
for key,value in a.items():
    print("4遍历字典健值",key + ':' + value)




#She is convinced that her path will come by herself