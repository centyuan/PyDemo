# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 9:39

from timeit import Timer
t_1=Timer('t=a;a=b;b=t','a=2;b=3').timeit()
t_2=Timer('a,b=b,a','a=4;b=5').timeit()
print(t_1,t_2)

"""
相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具
"""