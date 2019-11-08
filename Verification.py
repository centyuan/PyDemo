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

{"send_award_rules":{"torre":{"3":{"fixed_amount":"12.88","ratio":0},"4":{"fixed_amount":"212.88","ratio":0},"5":{"fixed_amount":"812.88","ratio":0},"6":{"fixed_amount":0,"ratio":"5"},"7":{"fixed_amount":0,"ratio":"10"}},"comfort":{},"consumption":{}},"accept_award_rules":{"specialamount":{"1.23":{"fixed_amount":"12.88","ratio":0},"2.34":{"fixed_amount":"12.88","ratio":0},"3.45":{"fixed_amount":"12.88","ratio":0},"4.56":{"fixed_amount":"12.88","ratio":0},"5.67":{"fixed_amount":"12.88","ratio":0},"6.78":{"fixed_amount":"12.88","ratio":0},"7.89":{"fixed_amount":"12.88","ratio":0},"9.87":{"fixed_amount":"12.88","ratio":0},"8.76":{"fixed_amount":"12.88","ratio":0},"7.65":{"fixed_amount":"12.88","ratio":0},"6.54":{"fixed_amount":"12.88","ratio":0},"5.43":{"fixed_amount":"12.88","ratio":0},"4.32":{"fixed_amount":"12.88","ratio":0},"3.21":{"fixed_amount":"12.88","ratio":0},"1.11":{"fixed_amount":"18.88","ratio":0},"2.22":{"fixed_amount":"18.88","ratio":0},"3.33":{"fixed_amount":"18.88","ratio":0},"4.44":{"fixed_amount":"18.88","ratio":0},"5.55":{"fixed_amount":"18.88","ratio":0},"6.66":{"fixed_amount":"18.88","ratio":0},"7.77":{"fixed_amount":"18.88","ratio":0},"8.88":{"fixed_amount":"12.88","ratio":0},"9.99":{"fixed_amount":"12.88","ratio":0},"0.01":{"fixed_amount":"18.88","ratio":0},"5.20":{"fixed_amount":"18.88","ratio":0},"13.14":{"fixed_amount":"18.88","ratio":0},"11.11":{"fixed_amount":"18.88","ratio":0},"22.22":{"fixed_amount":"18.88","ratio":0},"33.33":{"fixed_amount":"18.88","ratio":0},"44.44":{"fixed_amount":"18.88","ratio":0},"55.55":{"fixed_amount":"18.88","ratio":0},"12.34":{"fixed_amount":"18.88","ratio":0},"23.45":{"fixed_amount":"18.88","ratio":0},"34.56":{"fixed_amount":"18.88","ratio":0},"45.67":{"fixed_amount":"18.88","ratio":0},"56.78":{"fixed_amount":"18.88","ratio":0},"67.89":{"fixed_amount":"18.88","ratio":0}},"packagenumber":{},"comfort":{"4":{"fixed_amount":"312.88","ratio":0},"5":{"fixed_amount":"812.88","ratio":0},"6":{"fixed_amount":"2812.88","ratio":0},"7":{"fixed_amount":"666.66","ratio":0},"8":{"fixed_amount":"28812.88","ratio":0},"9":{"fixed_amount":0,"ratio":"5"},"10":{"fixed_amount":0,"ratio":"10"},"11":{"fixed_amount":0,"ratio":"15"},"12":{"fixed_amount":0,"ratio":"20"},"13":{"fixed_amount":0,"ratio":"30"}}}}