# 《python高性能编程》
# 1.使用功能time计时
import random
from timeit import Timer

t_1 = Timer('t=a;a=b;b=t', 'a=2;b=3').timeit()
t_2 = Timer('a,b=b,a', 'a=4;b=5').timeit()
print('方式1:',t_1, t_2)
# 2. 使用linux命令/usr/bin/time -p python timefn.py
"""
Length of x: 1000 
Total elements: 1000000 
calculate_z_serial_purepython took 12.7298331261 seconds 
real 13.46 
user 13.40 
sys 0.04
• real 记录了整体的耗时。
• user 记录了 CPU 花在任务上的时间，但不包括内核函数耗费的时间。
• sys 记录了内核函数耗费的时间。
"""


# 3.使用cProfile(profile:原始的纯python分析器,hotshot等)
# 相对于 timeit 的细粒度，cProfile,profile 和 pstats 模块提供了针对更大代码块的时间度量工具
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
print('方式二:',cProfile.run('f1(lIn)'))
print('方式二:',cProfile.run('f2(lIn)'))
"""
ncalls：表示函数调用的次数； 
tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
percall：（第一个 percall）等于 tottime/ncalls； 
cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
percall：（第二个 percall）即函数运行一次的平均时间，等于 cumtime/ncalls； 
filename:lineno(function)：每个函数调用的具体信息；
"""

# 4. line_profiler:逐行分析(CPU密集型性能问题最强大工具,先使用cProfile找到函数,line_profile对函数逐行分析)
# pip install line_profiler
# usage:kernprof -l -v timefn.py  # -l代表逐行分析,-v用于显示输出

# 4.memory_profiler:以图的形式展示RAM使用情况随时间变化
# pip install memory_profiler 或 pip install psutil
# usage:python -m memory_profiler timefn.py

# 4. heapy:追踪python内存中所有对象,用户查找内存泄露



# 5. perf/stat

