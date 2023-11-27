import time, random, os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process, Pool, synchronize

# synchronize包含一些同步原语:Lock、Condition、Semaphore、Event


# 一:四种创建进程的方式
# 1.multiprocessing.Process创建实例
def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


def long_tima_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


if __name__ == "__main__":
    print("父进程 %s." % os.getpid())
    p = Process(target=run_proc, args=("test",))  # target传入任务执行函数
    print("开启新进程.")
    p.start()
    p.join()  # 等待子进程结束
    print("新进程结束.")
    print("父进程结束%s." % os.getpid())


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
        # ps.apply(worker,args=(i,))          # 1.同步执行
        ps.apply_async(worker, args=(i,))  # 2. 异步执行
    """
    也可以使用map
    result = ps.map(worker,[1,2,3,4])  # 接受一个可迭代对象，将每个元素作为参数传递给worker
    """
    ps.close()  # 关闭线程池,停止接收其他线程
    ps.join()  # 调用join()方法会等待所有子进程执行完毕在向下执行,调用join()之前必须先调用close()  # 等待子进程结束, 阻塞父进程
    print("主进程终止")


# 4. concurrent.futures.ProcessPoolExecutor 进程池
def task_(sleep_sec=10, tag="test"):
    print("[%s] start sleep" % tag)
    time.sleep(sleep_sec)
    print("[%s] finish sleep" % tag)
    return 100


def main4():
    process_pool = ProcessPoolExecutor(max_workers=3)
    future = process_pool.submit(task_, 3, tag="TEST")
    ret = future.result()
    print("result is %s" % str(ret))
    process_pool.shutdown()


# 5.subprocess 创建新进程(subprocess.run 或 subprocess.Popen)
stdout, stderr = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()


# 多进程的异常处理
"""
进程池Pool管理时候,当一个进程发生异常,这个进程会被销毁,并重新启动一个进程,
并且异常会被记录到进程池内部队列，而不是抛出到主进程中
如果不主动检查这个队列，那么就无法知道进程中发生了什么异常
为避免这种情况需要加入异常处理机制


import multiprocessing

def worker():
    try:
        for i in range(3):
            print(f"Process {multiprocessing.current_process().pid} is running")
            time.sleep(1)
        raise Exception("Process error")
    except Exception as e:
        print(f"Process {multiprocessing.current_processs().pid} is raising {e})
        raise e
    
if __name__ == "__main__":
    pool = multiprocessing.Pool(2)
    try:
        pool.apply_async(worker)
        pool.apply_async(worker)
        pool.close()
        pool.join()
    except Exception as e:
        print(f"Main process is raisng {e}")

# 使用了 try-except 结构来捕获进程池中的异常，并将其抛出到主进程中  


# 回调函数处理异常
import multiprocessing 
import time 

def worker():
    for i in range(3):
        print(f"Processing {multiprocessing.current_process().pid} is running )
        time.sleep(1)
    raise Exception("Process error")

def handle_result(result):
    if isinstance(result, Exception):
        print(f"Pool is raising {result}")

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    try:
        pool.apply_async(worker, callback=handle_result)
        pool.apply_async(worker, callback=handle_result)
        pool.close()
        pool.join()
    except Exception as e:
        print(f"Main process is raising {e}")
"""
