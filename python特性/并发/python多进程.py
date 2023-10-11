import time, random, os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process, Pool, synchronize
# synchronize包含一些同步原语:Lock、Condition、Semaphore、Event

# 一:四种创建进程的方式
# 1.multiprocessing.Process创建实例
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_tima_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('父进程 %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # target传入任务执行函数
    print('开启新进程.')
    p.start()
    p.join()  # 等待子进程结束
    print('新进程结束.')
    print('父进程结束%s.' % os.getpid())


# 2. 继承mutliprocesing.Process,重写run方法
class MyProcess(Process):
    def __init__(self):
        Process.__init__()

    def run(self):
        print("子进程开始>>> pid={0},ppid={1}".format(os.getpid(), os.getppid()))
        time.sleep(2)
        print("子进程终止>>> pid={}".format(os.getpid()))


def main2():
    print("主进程开始>>> pid={}".format(os.getpid()))
    myp = MyProcess()
    myp.start()
    # myp.join()
    print("主进程终止")


# 3.使用进程池 multiprocessing.Pool
def worker(arg):
    print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))
    time.sleep(0.5)
    print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))


def main3():
    print("主线程开始执行>>> pid={}".format(os.getpid()))
    ps = Pool(5)
    for i in range(10):
        # ps.apply(worker,args=(i,))          # 同步执行
        ps.apply_async(worker, args=(i,))  # 异步执行

    ps.close()  # 关闭线程池,停止接收其他线程
    ps.join()  # 调用join()方法会等待所有子进程执行完毕在向下执行,调用join()之前必须先调用close()  # 等待子进程结束, 阻塞父进程
    print("主进程终止")


# 4. concurrent.futures.ProcessPoolExecutor 进程池
def task_(sleep_sec=10, tag='test'):
    print('[%s] start sleep' % tag)
    time.sleep(sleep_sec)
    print('[%s] finish sleep' % tag)
    return 100


def main4():
    process_pool = ProcessPoolExecutor(max_workers=3)
    future = process_pool.submit(task_, 3, tag='TEST')
    ret = future.result()
    print('result is %s' % str(ret))
    process_pool.shutdown()

# 5.subprocess 创建新进程(subprocess.run 或 subprocess.Popen)
 stdout, stderr = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()