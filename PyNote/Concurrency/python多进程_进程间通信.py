"""
进程间的通信(进程之间的内存空间相互隔离):
1.管道pipe,单方向通信/具有亲缘关系的进程间通信(父子/兄弟)
2.命名管道FIFO,一个存在于硬盘上的文件,可用于任何两个进程间的通信
3.消息队列,multiprocessing.Queue() 在内存中开辟队列结构
4.信号量Semaphore,本质是一种数据操作锁,用于负责数据操作过程中的互斥和同步
5.共享内存,效率最高的(由于没有相应的互斥机制,一般和信号量搭配使用)
6.信号signal
7.套接字socket
8.文件

一般有三种方式:
1.multiprocessing.Queue()
2.multiprocessing.Pipe()
3.multiprocessing.Manager()
python中一共有三个Queue:
1.queue.Queue(),用于线程间通信
2.multiprocessing.Queue(),用于进程间通信
3.multiprocessing.Manager().Queue(),用于使用进程池创建的进程通信
"""
import os
import random
import time
from multiprocessing import Process
from multiprocessing import Semaphore, Pipe, Queue,Manager

# 1.管道pipe,本质上是内核中的一个缓存,
# one:使用os.pipe()
# r, w = os.pipe()  # 创建管道,返回(r,w)读取/写入的文件描述符
# input_data = "hello world".encode("utf-8")
# os.write(w, input_data) #
# output_data = os.read(r, len(input_data))
# print("输出:",output_data.decode("utf-8"))


# two:使用功能multiprocessing.Pipe
# fd_r, fd_w = Pipe()
#
#
# def write_(name):
#     time.sleep(3)
#     fd_w.send("发送字符串到管道" + str(name))
#     print(os.getppid(), "---", os.getpid())
#
#
# def main():
#     jobs = []
#     for i in range(3):
#         p = Process(target=write_, args=(i,))
#         jobs.append(p)
#         p.start()
#     for i in range(3):
#         data = fd_r.recv()
#         print(data)
#     for job in jobs:
#         job.join()

# 2.消息队列 multiprocessing.Queue
queue = Queue()
queue.put("写入消息")
queue.get()  # 读取消息

# 3.共享内存 multiprocessing.Value/multiprocessing.Array/multiprocessing.Manager
manager = Manager()



# 4.信号量
# def move_(name, sem):
#     sem.acquire()  # 获取锁`
#     print("moving %s" % name)
#     time.sleep(random.randint(1, 4))
#     print("exit")
#     sem.release()  # 释放锁
#
#
# # 设置四把锁
# sem = Semaphore(4)
# for i in range(8):
#     p = Process(target=move_, args=(i, sem))
#     p.start()
