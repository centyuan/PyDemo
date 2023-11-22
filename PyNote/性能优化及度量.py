from time import time

"""一:改进算法,选择合适的数据结构,优化时间复杂度"""

# 1.使用dict查找元素而不是list,或者set(list)
"""
dict使用了hash table，因此查找操作时间复杂度为O(1),

"""
t = time()
list_demo = ['a', 'b', 'is', 'python', 'jason', 'hello', 'phone', 'test', 'apple', 'ind', 'var', 'bana']
# list_demo = dict.fromkeys(list,True)
filter = []
for i in range(1000000):
    for find in ['is', 'hat', 'new', 'list', 'old', '.']:
        if find not in list_demo:
            filter.append(find)
print('花费时间:', time() - t)

# 2.使用set求交集而不是list
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 34, 53, 42, 44]
listb = [2, 4, 6, 9, 23]
intersection = []
# 使用list
for i in range(100):
    for a in lista:
        for b in listb:
            if a == b:
                intersection.append(a)
# 使用set
for i in range(100):
    list(set(lista) & set(listb))

# 3.字符串优化
# (使用join而不是+)
# (字符串可以使用正则表达式或者内置函数来处理时候,选择内置函数，如str.startswith)

# 4.使用列表解析(要比在循环中重新构建一个新的 list 更为高效),推导式或生成器表达式

# 5.合理使用copy,deepcopy(deepcopy使用递归复制,慢一个数量级)

# 6.在循环开始之前:设置一个局部变量保存一个函数的全局引用(或其他模块)(字典查询在大量调用时会降低性能)
# python访问一个变量,函数或模块时步骤:1.查找本地变量locals(),2.查找全局变量globals(),3.查找__builtin__模块对象(实际上在模块对象的locals()查找)
# 7.其他xrange代替range(python3：range代替xrange)

# 8.使用局部变量,避免global，局部变量比全局变量快

# 9.is运算符比==速度快,能用is情况尽量使用

# 10.if done is not None 比 if done !=None快,if done is True比if done ==True快一倍

# 11.(交换变量值:a,b=b,a)

# 12.while 1比while True快(后者可读性强，True是一个全局变量而非关键字)

# 13.内建函数通常较快,add(a,b)优于a+b

# 14.优化循环:循环外能做的事放在循环外面

# 15.优化包含多个判断(对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面)ps:充分利用Lazy-evaluation

# 16.使用最佳的反序列化方式(eval,cPickle,json) json比cPickel快3倍,比eval快20倍
"""
  采用了RPython编写的PyPy是一个专为Python配备的即时JIT编译器，RPython是Python的一个静态类型的子集，不同于CPyton解释器，PyPy对源代码进行编译，生成CPU可直接运行的机器码。
  由于JIT特性，执行速度更快，长时间运行的应用更能从缓冲中受益，大部分的C扩展模块都在PyPy中得到支持,根据官网的基准测试数据，它比CPython实现 的Python要快6倍以上
  由于历史原因，目前pypy中 还保留着GIL，不过正在进行的STM项目试图将PyPy变成没有GIL的Python。
  如果python程序中含有C扩展(非cffi的方式)，JIT的优化效果会大打折扣，甚至比CPython慢（比 Numpy）。
  所以在PyPy中最好用纯Python或使用cffi扩展。 随着STM，Numpy等项目的完善，相信PyPy将会替代CPython。
  详细描述了CPython和PyPy的不同：https://doc.pypy.org/en/latest/cpython_differences.html
"""

""" 性能度量及性能瓶颈定位"""
# 参考《python高性能编程》
# 1.计时time模块(time.perf_counter()/time.process_time()或者timeit模块
import random
from timeit import Timer
import timeit 

t_1 = Timer('t=a;a=b;b=t', 'a=2;b=3').timeit()
t_2 = Timer('a,b=b,a', 'a=4;b=5').timeit()
t_3 = timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)
print('方式1:',t_1, t_2,t_3)
# python -m timeit "x=(1,2,3)"
"""
time.perf_counter():会计算sleep时间
time.process_time():不会计算sleep时间
python3.7以上提供三个精确到纳秒的计时:
time.perf_couter_ns()
time.process_time_ns()
time.time_ns()
"""



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
filename:lineno(function)：stall每个函数调用的具体信息；
"""

# 4. line_profiler:逐行分析(CPU密集型性能问题最强大工具,先使用cProfile找到函数,line_profile对函数逐行分析)
# pip install line_profiler
# usage:kernprof -l -v timefn.py  # -l代表逐行分析,-v用于显示输出

# 4.memory_profiler:以图的形式展示RAM使用情况随时间变化
# pip install memory_profiler 或 pip install psutil
# usage:python -m memory_profiler timefn.py

# 4. heapy:追踪python内存中所有对象,用户查找内存泄露

# 5.py-spy

# 6. perf/stat

