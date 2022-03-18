# -*- coding:utf-8 -*-


#主要是前面的 *
#args可变参数,传入的参数数量是可变的,可以多个,可以0个
#kwargs关键字参数
#但必须按顺序写，否则会报错，顺序为（位置参数，默认参数，可变参数，命名关键字参数，关键字参数）
#位置参数,默认参数(默认参数必须指向不变对象,int string,tuple),可变参数,命名关键字参数,关键字参数
#在tuple或list前加一个*，构造出可变参数,在dict前加两个*，构造关键字参数。

L=(1,2,3)
def fun_var_args(farg, *args):
    print("fun_var_args farq:", farg)
    print('func_var_args args:',args)
    print('type(args):',type(args))#元组tuple
    for value in args:
        print( "another arg:", value,type(value))


fun_var_args(1, "two", 3)
fun_var_args(1,*L) #L为元组#或列表
#前面的 **的用法
bl={
    'myarg2':'myarg2_num',
    'myarg3':'myarg3_num',
    'test':'test_num',
}
def fun_var_kwargs(farg, **kwargs):
    print("fun_var_kwargs arg:", farg)
    print('func_var_kwargs:',type(kwargs))#kwargs为字典dict
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
