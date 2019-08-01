# -*- coding:utf-8 -*-


#主要是前面的 *
#args可变位置参数
#kwargs可变关键字参数
def fun_var_args(farg, *args):
    print("arg:", farg)
    print(args)
    print(type(args))#元组tuple
    for value in args:
        print( "another arg:", value)
        print(type(value))

fun_var_args(1, "two", 3)

#前面的 **的用法
bl={
    'myarg2':'myarg2_num',
    'myarg3':'myarg3_num',
    'test':'test_num',
}
def fun_var_kwargs(farg, **kwargs):
    print("arg:", farg)
    print(type(kwargs))#kwargs为字典dict
    a=kwargs["myarg3"]
    print(kwargs["myarg2"])
    print(a)
    for key in kwargs:
        print( "another keyword arg: %s: %s" % (key, kwargs[key]))


def au_login(hot=False,statusStorageDir='itchat.pkl',
            enableCmdQR=False):
    print("hot:",hot)
    print("statusStorageDir:",statusStorageDir)
    print("enableCmdQR:",enableCmdQR)

fun_var_kwargs(farg=1, myarg2="two", myarg3=3)
# myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
fun_var_kwargs(farg=1,**bl)
au_login(True)#使用关键字参数，可以不传入参数名，按顺序一样
