---
title: GIL和垃圾回收机制
categories: 
   - Python从入门到放弃
tags: 
   - python
---

### 一:GIL

#### 1. GIL是什么?

>Global interperter Lock是全局解释器锁(并不是python的特性,CPython时所引入的概念,python完全可以不依赖GIL)
>
>每个线程在执行过程都要先获取GIL,保证同一时刻只有一个线程运行,目的是解决多线程之间数据完整性和状态同步,在单核CPU时代对Python有积极作用,在多核CPU时代,阻碍了python在多核cpu的并发。
>
>[pep-703](https://peps.python.org/pep-0703/)提案使Cpython有望告别GIL

#### 2.为什么选择GIL？

相比使用更细粒度的锁，GIL具有一下优点:

>1: 单线程本质是顺序执行，有更好的性能表现
>
>2: 大大简化了python线程中的共享资源的管理，包装C库更容易，不必担心线程安全
>
>3: 对于 I/O 密集型来说，在多线程情况下速度更快
>
>4: 对内存管理的引用计数，有效解决了线程安全问题(因为引用计数管理内存,所以某个对象的引用计数不能被两个线程同时增加和减少,或内存泄露:GIL对线程间共享的所有数据结构加锁可以保证引用计数变量的安全性)



#### 3.GIL什么时候释放

>1.协同式多任务处理：IO密集型的操作，在较长的或者不确定的时间(IO阻塞，python标准库中所有阻塞性I/O和time.sleep()都会释放GIL)，没有运行Python代码的需要，线程便会让出GIL
>
>2.抢占式多任务处理：CPU密集型的操作，解释器运行一段时间就主动释放GIL，这种机制叫间隔式检查（check_interval）,每隔一段时间Python解释器就会强制当前线程去释放 GIL而不需要经过正在执行代码的线程允许，这样其他线程便能运行。
>
>(在python3中，这个时间间隔是15毫秒)

#### 4.GIL缺陷

  >1:抢占式多任务处理(CPU密集型):
  >
  >每个线程在多个cpu交替执行:cpu调度线程唤醒->去拿GIL->没拿到->在等待:1.线程上下文切换,2.争抢不到GIL会让cpu等待,都浪费cpu时间
  >
  >2:Python的每个版本中也在逐渐改进GIL和线程调度之间的互动关系。例如先尝试持有GIL在做线程上下文切换，在IO等待时释放GIL等尝试,但是无法改变的是GIL的存在使得操作系统线程调度的这个本来就昂贵的操作变得更奢侈了



#### 5.避免GIL

**1.使用多进程编程，每个进程都有自己的解释器和内存空间**

> multiprocess替代Thread,每个进程都有独立的GIL,但是它的引入会增加程序实现时线程间数据通讯和同步的困难

**2.使用cython避开全局锁**

>cython通常用于处理计算密集型的任务，以加快python程序总体运行速度

**3.使用其他python解释器**

>PyPy:是用RPython(CPython的子集)实现的Python，根据官网的基准测试数据，它比CPython实现 的Python要快6倍以上。
>
>虽然也有GIL，但是使用了Just‑in‑Time(JIT)编译器，即动态编译器，与静态编译 器(如gcc,javac等)不同，它是利用程序运行的过程的数据进行优化。
>
>Pyston:从CPyhton解释器衍生出的分支，实现了性能优化，有可能加速高达30%，由于缺乏兼容的二进制包，需要重新编译
>
>RustPython:由Rust编写的Python解释器，RustPython和CPython类似，但可以选择启用JIT编译器

#### 6.GIL是否意味线程绝对安全

>GIL不是意味线程绝对安全
>
>在协同式多任务处理情况时，线程是安全的，不需要额外在更细粒度的锁
>
>在抢占式多任务处理情况时, GIL被强制释放时候，可能会出现线程不安全

如下，两个线程对全局变量进行了1000000次加和减，如果线程安全的，则n为0

```python
import threading
n = 0

def add():
    global n
    for i in range(1000000):
        n = n+1

def sub():
    global n 
    for i in range(1000000):
        n = n-1
if __name__ == "__main__":
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("n的值:",n)
```

下面对比下add和sub字节码执行过程

```python
from dis import dis
n = 0
def add():
    global n
    n = n + 1
def sub():
    global n
    n = n - 1

print(dis(add))
print(dis(sub))
```

```text
 44           0 LOAD_GLOBAL              0 (n)
              2 LOAD_CONST               1 (1)
              4 BINARY_ADD
              6 STORE_GLOBAL             0 (n)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
None
 47           0 LOAD_GLOBAL              0 (n)
              2 LOAD_CONST               1 (1)
              4 BINARY_SUBTRACT
              6 STORE_GLOBAL             0 (n)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
None
```

>LOAD_GLOBAL:加载全局变量
>
>LOAD_CONST: 加载常量
>
>BINARY_ADD/BINARY_SUBTRACT:进行二进制加减法
>
>STORE_GLOBAL:将计算结果保存到全局变量n
>
>加法减法操作不是原子级的，所以当GIL被强制释放的时候，上面执行某一步被中断,引起线程安全问题

### 二:垃圾回收机制

**python垃圾回收机制:**

> 1.引用计数机制
>
> 2.标记-清除 mark and sweep:首先标记对象（垃圾检测），然后清除垃圾（垃圾回收）
>
> 3.分代收集 generation collection:这种思想简单点说就是：对象存在时间越长，越可能不是垃圾，应该越少去收集
>
> 引用计数为主，分代收集和标记-清除为辅
>
> 三种情况触发垃圾回收
> 1、调用gc.collect()
> 2、GC达到阀值时
> 3、程序退出时

#### 1.引用计数机制(Reference Counting)

>(1:PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。
>
>(2:对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少
>
>(3:当引用计数为0时，该对象生命就结束了。
>
>优点:简单,内存直接释放,实时性高,处理内存回收的时间分摊了
>
>缺点:维护引用计数需要消耗额外的资源,不能解决对象的循环引用问题

#### 2.标记清除(Mark and Sweep)

>1.基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发
>
>2.遍历以对象为节点、以引用为边构成的图
>
>(可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。)
>
>再次遍历:把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。
>
>优点: 基于追踪回收,分为标记阶段和回收阶段,解决了容器对象可能产生的循环引用问题
>
>只有容器对象才会产生循环引用情况
>
>缺点:必须扫描整个内存

#### 3.分代回收(Generational Collection)

>
>
>将内存根据对象存活的时间分为不同的集合(年轻代:0,中年代:1,老年代:2),对应三个链表
>
>1.新创建的对象分配在年轻代,年轻代链表总数达到上限会触发回收机制,可以回收的对象回收,不能回收的被移到中年代
>
>2.老年代存活时间最长,甚至整个系统的生命周期
>
>触发机制:当某世代中被分配的对象与被释放的对象之差达某一阈值,且比该代年轻的代也会被扫描
>
>查看各世代阈值:
>
>```python
>import gc
>print("各世代的阈值:",gc.get_threshold())
># 设置各世代阈值
>gc.set_threshold(800, 20, 20)
>```
>
>优点:
>
>执行垃圾回收过程中，程序会被暂停，即stop-the-world为了减少程序的暂停时间，采用分代回收(Generational Collection)降低垃圾收集耗时,是一种空间换时间的方式



参考资料:

[Python字节码介绍](https://zhuanlan.zhihu.com/p/39259061)

[Why Was Python Written with the GIL?](https://link.zhihu.com/?target=https%3A//softwareengineering.stackexchange.com/questions/186889/why-was-python-written-with-the-gil)

[Python中的垃圾回收机制](https://zhuanlan.zhihu.com/p/62282961)

[垃圾回收机制](https://zhuanlan.zhihu.com/p/83251959)