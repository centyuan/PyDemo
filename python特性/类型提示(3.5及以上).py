# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/1 10:41

from typing import Set
from typing import List
from typing import Tuple
from typing import Dict

def foo(a:str, b:str) ->str:
    c = None # type:str
    print("类型提示功能")
    print(a, b)
    return 'hi'

def calc_num(x:List[int]) ->str:
    sum = 0
    for ele in x:
        sum += ele
    return sum

class Student:
    def __init__(self):
        self.name = None # type:str


if __name__ == "__main__":
    foo('yuan', 'huai')
    student = Student()
    print(calc_num([1,2]))
    calc_num()
    m:Dict[int,int] =[1,2]



