from functools import wraps
import time

"""
使用装饰器时，有一些细节需要注意：被装饰后的函数其实已经是另一个函数了，它的函数名及属性等，都是属于新函数，
所以,Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用
"""
def timefn(fn):
    @wraps(fn)
    def measure_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2=time.time()
        print("timefn:"+fn.func_name+"took"+str(t2-t1)+"seconds")

"""
timeit 模块暂时禁用了垃圾收集器。如果你的操作会调用
到垃圾收集器，那么它有可能影响到你实际操作的速度
#有问题
usage: python -m timeit -n 5 -r 5 xx.py
循环次数（-n 5）
重复次数（-r 5）
循环执行n 次并计算平均值作为一个结果，重复r 次并选出最好的那个结果。
"""