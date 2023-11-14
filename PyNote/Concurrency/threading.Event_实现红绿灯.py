import random
import time
import threading

# 事件管理标志
event = threading.Event()  # 通过threading.Event()生成一个event对象和对象的引用event
"""
event对象重要特点是被设置为真时，会唤醒所有等待的它的进程
如果只想唤醒单个线程，最好使用信号量或者Condition对象代替
"""

def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m---green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m---yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m---red light on---\033[0m')
        else:
            count = 0  # 打开绿灯
            event.set()  # 休眠1s才能让car()有机会获取CPU的执行权
        time.sleep(1)
        count += 1


def car(n):
    while 1:
        time.sleep(random.randrange(3, 10))  # 休眠3s到10s（随机）才能让light()有机会获取CPU的执行权
        print("当前light()中isSet的状态:",event.isSet())  # 打印当前light()中isSet的状态
        if event.isSet():
            print("car [%s] is running..." % n)
        else:
            print('car [%s] is waiting for the red light...' % n)  # event.wait()    #红灯状态下调用wait方法阻塞，汽车等待状态


if __name__ == '__main__':
    car_list = ['aa', 'bb', 'cc']
    Light = threading.Thread(target=light)  # 创建一个以light为目标的线程任务
    Light.start()  # 启动线程
    for i in car_list:
        t = threading.Thread(target=car, args=(i,))  # 创建一个以car方法的线程任务，传car数组
        t.start()  # 启动t线程
