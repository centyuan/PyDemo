# -*- coding:utf-8 -*-
"""
1.args可变参数,传入的参数数量是可变的,可以多个,可以0个
2.kwargs关键字参数
3.顺序为（位置参数，默认参数，可变参数，命名关键字参数，关键字参数）
位置参数,默认参数(默认参数必须指向不变对象,int string,tuple),可变参数,命名关键字参数,关键字参数
# recv(maxsize, *, block) blck为关键字参数
4.前加一个*，构造出可变参数,如果定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
(命名关键字参数:限制关键字参数的名字,传参时必须传入参数名 如下: )
def person(name,age,*,city='beijing',job)
    pass
person('yuan',24,job='Engineer') # 命名关键字参数city具有默认值，调用时，可不传入city参数
5.在dict前加两个*，构造关键字参数。
"""
# 1.*args
L = (1, 2, 3)


def fun_var_args(farg, *args):
    print("fun_var_args farq:", farg)
    print('func_var_args args:', args)
    print('type(args):', type(args))  # 元组tuple
    for value in args:
        print("another arg:", value, type(value))


# usage
fun_var_args(1, "two", 3)
fun_var_args(1, *L)  # L为元组#或列表

# 2.**kwagrs
bl = {
    'myarg2': 'myarg2_num',
    'myarg3': 'myarg3_num',
    'test': 'test_num',
}


def fun_var_kwargs(farg, **kwargs):
    print("fun_var_kwargs arg:", farg)
    print('func_var_kwargs:', type(kwargs))  # kwargs为字典dict
    a = kwargs["myarg3"]
    print(kwargs["myarg2"])
    print(a)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))


fun_var_kwargs(farg=1, myarg2="two", myarg3=3)
# myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
fun_var_kwargs(farg=1, **bl)


# 3.默认参数
def au_login(hot=False, statusStorageDir='itchat.pkl',
             enableCmdQR=False):
    print("hot:", hot)
    print("statusStorageDir:", statusStorageDir)
    print("enableCmdQR:", enableCmdQR)


au_login(True)  # 使用关键字参数，可以不传入参数名，按顺序一样


# 4.args kwargs 两种传参方式

def test_args(*info):
    print(info)


def test_kwargs(**info):
    print(info, info.keys(), info.values())


tuple_data = ("name", "age", "man")
dict_data = {'name': 'yuan', 'age': 20, 'sex': 'man'}

test_args("name", "age", "man")
test_args(*tuple_data)

test_kwargs(a="a", b="123", c="234")
test_kwargs(**dict_data)
