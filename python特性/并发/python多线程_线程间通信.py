"""
queue.Queue()
threading.Event
threading.Condition
"""
# 一:全局变量(全局变量)+锁与同步
# threading.Lock()
# threading.RLock() 允许在同一个线程中多次acquire
# treading.Condition() 更高级锁
# threading.Semaphore() 内部管理着一个计数器。调用 acquire() 会使这个计数器 -1，release() 则是+1(可以多次release()，
# threading.Event() 全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞；如果“Flag”值为True，那么执行event.wait 方法时便不再阻塞。
# 死锁问题,两个线程都执行函数,并获取直接线程锁,调用对方对象的方法
"""
http://c.biancheng.net/view/2620.html
如何避免死锁:
1.避免在一个线程里,对多个Lock进行锁定,acquire
2.需要多个Lock锁定时,按照相同的加锁顺序
3.使用定时锁,acquire()可指定timeout参数
4.死锁检测::是一种依靠算法机制来实现的死锁预防机制，它主要是针对那些不可能实现按序加锁，也不能使用定时锁的场景的
"""
import threading

balance = 0
lock = threading.Lock()


def change_money(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000):
        # 获取锁
        lock.acquire()
        try:
            change_money(n)
        finally:
            lock.release()


if __name__ == '__main__':
    t1, t2 = threading.Thread(target=run_thread, args=(10,)), threading.Thread(run_thread, args=(20,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

# 二:queue.Queue()队列queue,安全的数据传递方式
from queue import Queue


class Student:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}:到!")


class Teacher:
    def __init__(self, queue):
        self.queue = queue

    def call(self, student_name):
        if student_name == "exit":
            print("点名结束,开始上课")
        else:
            print(f"老师:{student_name}来了没?")
        self.queue.put(student_name)  # 入队,发送消息


class CallManager(threading.Thread):
    def __init__(self, queue):
        super(CallManager, self).__init__()
        self.queue = queue
        self.students = {}

    def put(self, student):
        self.students.setdefault(student.name, student)

    def run(self):
        while True:
            student_name = self.queue.get()
            if student_name == "exit":
                break
            elif student_name in self.students:
                self.students[student_name].speak()
            else:
                print(f"老师,咋班没有这个人{student_name}")


queue = Queue()
teacher = Teacher(queue=queue)
students = [Student(name=i) for i in ["张三", "李四", "王五"]]
cm = CallManager()
result = [cm.put(s) for s in students]
cm.start()
# 开始点名
teacher.call("李四")
teacher.call("王五")
teacher.call("李逵")
