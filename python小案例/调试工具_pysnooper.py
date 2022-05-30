import pysnooper
import math

# @pysnooper.snoop("debug.log")
@pysnooper.snoop()
def getprime(start,end):
    # 求素数
    p = []
    if start<=3:
        start = 3
    for i in range(start,end):
        flag = True
        for j in range(2,math.ceil(i**0.5)+1):
            if i%j ==0:
                flag = False
                break
        if flag:
            p.append(i)
    return p

getprime(100,110)