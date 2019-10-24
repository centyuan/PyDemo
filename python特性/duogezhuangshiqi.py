# -*- coding:utf-8 -*-
import time

def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper

@deco01
@deco02
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))



if __name__ == '__main__':
    f = func
    f(3,4)
    #func()

'''
this is deco01
this is deco02
hello，here is a func for add :
result is 7
deco02 end here
time is 1003 ms
deco01 end here
'''