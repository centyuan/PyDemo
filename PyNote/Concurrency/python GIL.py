"""
    GIL:Global interperter Lock全局解释器锁(并不是python的特性,CPython时所引入的概念,python完全可以不依赖GIL)
    1.GIL全局解释锁:每个线程在执行过程都要先获取GIL,保证同一时刻只有一个线程运行,目的是解决多线程之间数据完整性和状态同步。
    Python的多线程在多核CPU上，只对于IO密集型计算产生正面效果；而当有至少有一个CPU密集型线程存在，那么多线程效率会由于GIL而大幅下降

    2.因为引用计数管理内存,所以某个对象的引用计数不能被两个线程同时增加和减少,或内存泄露:GIL对线程间共享的所有数据结构加锁可以保证引用计数变量的安全性

    3. GIL锁的释放:
    ### 1.协同式多任务处理：IO密集型的操作，在较长的或者不确定的时间(IO阻塞，python标准库中所有阻塞性I/O和time.sleep()都会释放)，没有运行Python代码的需要，线程便会让出GIL；
    ### 2.抢占式多任务处理：CPU密集型的操作，解释器运行一段时间就主动释放GIL，这种机制叫间隔式检查（check_interval）,每隔一段时间Python解释器就会强制当前线程去释放 GIL而不需要经过正在执行代码的线程允许，这样其他线程便能运行。
    (在python3中，这个时间间隔是15毫秒)
    控制多线程同步的原语:Locks、RLocks、Semaphores、Events、Conditions和Barriers(python3.2之后引入)，还有Queue,可以继承这些类，实现自己的同步控制原语。

    4.GIL缺陷:
        1.抢占式多任务处理(CPU密集型):(每个线程在多个cpu交替执行:cpu调度线程唤醒->去拿GIL->没拿到->在等待:1.线程上下文切换,2.争抢不到GIL会让cpu等待,都浪费cpu时间)
        2.Python的每个版本中也在逐渐改进GIL和线程调度之间的互动关系。例如先尝试持有GIL在做线程上下文切换，在IO等待时释放GIL等尝试。
        3.但是无法改变的是GIL的存在使得操作系统线程调度的这个本来就昂贵的操作变得更奢侈了


    5.避免GIL(multiprocess替代Thread,每个进程都有独立的GIL)
    但是:它的引入会增加程序实现时线程间数据通讯和同步的困难

6.进程线程区别:
1根本区别:资源分配的基本单位,cpu跳读执行的基本单位
2地址空间:空间资源独立,共享本进程的空间和资源
3键壮性:崩溃不影响其他进程,一个线程崩溃整个进程崩掉
4执行过程:进程有(执行入口/顺序执行/执行开销大),线程不能独立运行(依附于进程,执行开销小)
5切换:进程切换资源消耗大,线程切换消耗小
(进程切换需要切换页表,页表切换后,TLB失效,地址转化时需要重新查找页表。线程切换不需要切换页表)

7. 进程切换
1.虚拟内存:内存耗尽时，用硬盘充当内存(把不常用的程序片断就放入虚拟内存，当需要用到它的时候在load入主存（物理内存）中)
2.每个进程都有属于自己的，私有的，地址连续的的虚拟内存
3.进程被创建时会建立一个 虚拟内从到物理内存的映射表--------页表，根据页表可以将虚拟内存和物理内存关联起来
  需要页表(地址空间映射)来记住虚拟地址空间中某个数据应该被放到那个物理内存地址
4.进程执行时,根据页表将数据load到相应的物理内存上
5.进程上下文:一个进程存储在处理器各寄存器中的中间数据
6.进程切换步骤: 
   1.切换新的页表，然后使用新的虚拟地址空间
   2.切换内核栈，加入新的内容(PCB控制块，资源相关)，硬件上下文切换
   注意：进程的切换需要设计到用户态到内核态的切换，因为无论是进程上下文切换还是线程上下文切换，都是计算机内核完成的
https://blog.csdn.net/weixin_44844089/article/details/115672685

8.进程和线程
单核cpu,单进程,单线程,线程始终在一个cpu上运行吗?
是
多核cpu,单进程,单线程,线程始终在一个cpu上运行吗?
默认不是,代码中可以绑定
多核cpu,单进程,多线程,多个线程并行在同一个cpu上还是某一时刻只有一个运行在cpu上,其他线程等待?
python GIL存在,一个进程只允许一个线程运行,但是这个线程会在不同cpu之间切换

9.线程状态
   1.创建new(分配资源，初始化)
   2.就绪ready
   3.执行running(获取CPU时间,执行代码)
   4.阻塞blocked(放弃CPU,暂停运行,常见阻是原因:等待I/O操,等待锁,等待其他线程通知)
   5.终止terminated()
  进程状态:
   1.运行running
   2.就绪ready
   3.等待wait
"""