from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
import threading
import time


# 一:ThreadPoolExecutor
# 回调函数
def get_result(future):
    print(future.result())


def Actioin(max, a, b, c):
    total = 0
    print(a + b + c)
    for i in range(max):
        print(threading.current_thread().name + ":" + str(i))
        total += 1
    return total


# 1.创建一个线程池
pool = ThreadPoolExecutor(max_workers=5)
future_1 = pool.submit(Actioin, 10, "yuan", "bingx", "xi")  # 提交一个task，并传入参数:传参不要元组，接着往后写，有多少写多少
future_2 = pool.submit(Actioin, 20, "君君", "臣臣", "父父")

# 2.添加回调函数
future_1.add_done_callback(get_result)
future_1.done()  # 判断任务是否结束
future_1.result()  # 获取任务返回的结果：.result()会阻塞当前线程，如果没有指定 timeout 参数，当前线程将一直处于阻塞状态，直到 Future 代表的任务返回
# future_1.cancel()  # 取消任务,如果任务已在线程池中运行,就取消不了
future_1.cancelled()  # 返回 Future 代表的线程任务是否被成功取消。
future_1.running()  # 如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True
future_1.exception(timeout=None)  # 获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None
# 3.等待线程池中的任务执行完后再执行其他线程
wait(future_1, return_when=FIRST_COMPLETED)  # return_when:表示wait返回结果的条件,FIRST_COMPLETED:表示完成第一个任务后就执行主线程

# 4. as_completed 使用as_completed方法一次取出所有任务的结果。
"""
as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务，
就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，先完成的任务会先通知主线程
"""
for future in as_completed([future_1, future_2]):
    message = future.result()
# 关闭线程池
pool.shutdown()

# 二: with
"""由于线程池实现了上下文管理协议（Context Manage Protocol），因此，程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池"""
# a = (10,"1","12","123")
# b = (20,"21","212","2123")
# c = (30,"31","312","3123")
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用map()来启动 3 个线程:元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(Actioin, (10, 30, 90))
    # results = pool.map(Actioin,(a,b,c))  error
