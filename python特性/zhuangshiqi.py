# -*- coding:utf-8 -*-
#带有参数的装饰器
import time

def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))


class Student(object):


    def score(self):
        return self._score

    @score
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == '__main__':
    f = func
    f(3,4)
    #func()
