# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/27 17:28

from typing import List
from random import randint

def fuzhi():
    global is_first
    print("fuzhi_before",is_first)
    is_first = False
    print("fuzhi_after",is_first)
def modi(is_first):
    print(is_first)
    for i in range(3):
        fuzhi()
        print(i)

is_first = True

if __name__ == "__main__":
    if not None:
        print(123)
    if None:
        print('234')
    randint

