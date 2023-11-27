"""
进程间的通信IPC,InterProcess Communication
(进程之间的内存空间相互隔离):
1.匿名管道pipe:单方向通信/具有亲缘关系的进程间通信(父子/兄弟)
2.命名管道FIFO:一个存在于硬盘上的文件,也是单方向通信,可用于任何两个进程间的通信
3.消息队列:multiprocessing.Queue() 在内存中开辟队列结构
4.信号量Semaphore:是一个计数器,常作为一种锁机制,用于负责数据操作过程中的互斥和同步
5.共享内存:创建一段其他进程都可以访问的内存,效率最高的(由于没有相应的互斥机制,一般和信号量搭配使用)
6.信号signal: 一种比较复杂的通信方式,用于通知接受进程间某个事件已经发生
7.套接字socket：也是一种通信机制,用于不同机器间通信
8.文件
9.锁: multiprocessing.Lock
Python中如何实现进程间通信?
常用的三种方式:
1.multiprocessing.Queue()
2.multiprocessing.Pipe()
3.multiprocessing.Array()
4.multiprocessing.Manager()一种更高级的进程间通信方式,创建一个用于进程间通信的共享对象,实现更为复杂的数据共享和通信


"""
import os
import random
import time
from multiprocessing import Process
from multiprocessing import Semaphore, Pipe, Queue, Manager

# 1.队列Queue,multiprocessing.Queue()
"""
import multiprocessing
def sender(queue):
    queue.put("hello")

def receiver(queue):
    msg = queue.get()
    print("received:", msg)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=sender, args=(queue,))
    p2 = multiprocessing.Process(target=receiver, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
"""
# 2.管道pipe,multiprocessing.Pipe() 本质上是内核中的一个缓存
"""
当管道满了或没数据可读,recv会阻塞
当管道满了或没空间可写,send会阻塞
Pipe:阻塞(会出现死锁问题)
Pipe:非阻塞(recv或send会立即返回一个IOError异常)
multiprocessing.Pipe(duplex=False)


import multiprocessing 

def sender(conn):
    conn.send("hello") # conn.write("hello".encode("utf-8"))
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print("received:",msg)
    conn.close()

if __name__ == "__main__":
    r_conn, w_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args(r_conn))
    p2 = multiprocessing.Process(target=receiver, args(w_conn))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
"""


# 3.共享内存 multiprocessing.Value/multiprocessing.Array/
"""
import multiprocessing

def write(n, arr):
    for i in range(n):
        arr[i] = i

def reader(n, arr):
    for i in range(n):
        print(arr[i])
    
if __name__ == "__main__":
    num = 5
    arr = multiprocessing.Array("i", num) # 将其转换为共享内存
    p1 = multiprocessing.Process(target=writer, args=(num, arr))
    p2 = multiprocessing.Process(target=reader, args=(num, arr))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


"""

# 4. multiprocessing.Manager
"""
import multiprocessing 

manager = multiprocessing.Manager()

shared_list = manager.list()  # 通过manager创建共享对象
shared_list.append(1)

#Manager还支持对象有:list/dict/Namespace/Value/Array/Lock/Barrier/Condition/Event/Semaphore


"""

# 5.信号量
"""
def move_(name, sem):
    sem.acquire()  # 获取锁`
    print("moving %s" % name)
    time.sleep(random.randint(1, 4))
    print("exit")
    sem.release()  # 释放锁


# 设置四把锁
sem = Semaphore(4)
for i in range(8):
    p = Process(target=move_, args=(i, sem))
    p.start()
"""


# 锁lock
"""
from multiprocessing import Process, Value,Lock


def sub(num):
    num.value +=1

if __name__ == "__main__":
    lock = Lock()
    val = Value("i", 0)  # Value是通过共享内存的方式共享数据 初始值 val 为0
    proc = [Process(target=sub, args=(val,)) for i in xrange(100)]
    
    for p in proc:
        p.start()
    for p in proc:
        p.join()

    print '经过100次累加之后 val 的值是: %d' %val.valu

"""
