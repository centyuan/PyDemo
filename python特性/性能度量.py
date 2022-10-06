# 1.使用功能time计时
import random
from timeit import Timer

t_1 = Timer('t=a;a=b;b=t', 'a=2;b=3').timeit()
t_2 = Timer('a,b=b,a', 'a=4;b=5').timeit()
print('方式1:',t_1, t_2)

"""
相对于 timeit 的细粒度，cProfile,profile 和 pstats 模块提供了针对更大代码块的时间度量工具
"""

# 2.使用cProfile
import cProfile


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]


def f2(lIn):
    l1 = [i for i in lIn if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]

lIn = [random.random() for i in range(100000)]
print(cProfile.run('f1(lIn)'))
print(cProfile.run('f2(lIn)'))
"""
ncalls：表示函数调用的次数； 
tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
percall：（第一个 percall）等于 tottime/ncalls； 
cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
percall：（第二个 percall）即函数运行一次的平均时间，等于 cumtime/ncalls； 
filename:lineno(function)：每个函数调用的具体信息；
"""