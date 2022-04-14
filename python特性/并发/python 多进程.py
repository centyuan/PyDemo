#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-3 下午2:07
from multiprocessing import Process,Pool
import time,random,os

#1. 创建Process实例,传入任务执行函数
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_tima_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':
    #一:
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    print('-------------')
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_tima_task,args=(i,)) #非阻塞
        #p.apply(long_tima_task,args=(i,)) #阻塞
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()#调用join()方法会等待所有子进程执行完毕在向下执行,调用join()之前必须先调用close()
    print('All subprocesses done.')
    #二
    #main()2


#2. 派生Process的子类,重写run方法
class MyProcess(Process):
    def __init__(self):
        Process.__init__()

    def run(self):
        print("子进程开始>>> pid={0},ppid={1}".format(os.getpid(), os.getppid()))
        time.sleep(2)
        print("子进程终止>>> pid={}".format(os.getpid()))

def main2():
    print("主进程开始>>> pid={}".format(os.getpid()))
    myp=MyProcess()
    myp.start()
    # myp.join()
    print("主进程终止")

#三 使用进程池

def worker(arg):
    print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))
    time.sleep(0.5)
    print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))

def main3():
    print("主线程开始执行>>> pid={}".format(os.getpid()))
    ps=Pool(5)
    for i in range(10):
        # ps.apply(worker,args=(i,))          # 同步执行
        ps.apply_async(worker, args=(i,))  # 异步执行
    ps.close() #关闭线程池,停止接收其他线程
    ps.join() #阻塞进程
    print("主进程终止")

