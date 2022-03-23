#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-10 下午3:00
import  copy
"""
直接赋值：其实就是对象的引用（别名）。
a[:]切片是浅拷贝

"""
#浅拷贝:拷贝父对象，不会拷贝对象的内部的子对象(父对象不是同一引用了，内部的子对象还是同一个引用)
a = {1:[1,2,3]}
b = a.copy()
print(a,b)

a[1].append(4)
print(a,b)

a[2] = [7,8,9]
print(a,b)


#深拷贝:copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象(完全独立，不存在相同引用)

c = copy.deepcopy(a)
print(a,c)
a[1].append(6)
print(a,c)



"""
解析：
1.赋值
 b = a ,a和b都指向同一个对象

2.浅拷贝
 b = a.copy()  a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）
 
3.深拷贝
 c = copy.deepcopy(a)  深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的
"""