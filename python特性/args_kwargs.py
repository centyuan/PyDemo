# -*- coding:utf-8 -*-


def fun_var_args(farg, *args):
    print("arg:", farg)
    print(args)
    print(type(args))#元组tuple
    for value in args:
        print( "another arg:", value)
        print(type(value))



fun_var_args(1, "two", 3)

def fun_var_kwargs(farg, **kwargs):
    print("arg:", farg)
    print(type(kwargs))#kwargs为字典dict
    a=kwargs["myarg3"]
    print(kwargs["myarg2"])
    print(a)
    for key in kwargs:
        print( "another keyword arg: %s: %s" % (key, kwargs[key]))
        print(key)

fun_var_kwargs(farg=1, myarg2="two", myarg3=3)  # myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
