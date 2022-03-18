# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/13 15:11
import copy
"""
直接赋值：其实就是对象的引用（别名）。b=a a和b都指向同一个对象

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。b=a.copy()a和b是一个独立的对象，但他们的子对象还是指向同一个对象

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。b=copy.deepcopy(a) 父对象和子对象都是独立的
"""

foo = [1,2]
foo1 = foo
foo.append(3)
print(foo,id(foo))
print(foo1,id(foo1))
dicts = {'one': 1, 'two': 2, 'three': 3}
tmp = dicts.copy()
tmp['one'] = 'abc'
print(dicts,id(dicts),tmp,id(tmp))
a={1:[1,2,3]}
b = a.copy()
print("copy:",a,id(a),b,id(b))
c = copy.deepcopy(a)
a[1].append(7)
print("deepcopy:",a,id(a),c,id(c))

def outer(fn):

    print('outer')

    def inner():

        print('inner')

        return fn

    return inner
@outer
def fun():
    print('fun')
fn=fun()
