# class HauntedBus:
#     def __init__(self, passengers=[]) -> None:
#         self.passengers = passengers
#     def pick(self, name):
#         self.passengers.append(name)
#     def drop(self, name):
#         self.passengers.remove(name)

# bus1 = HauntedBus()
# print(bus1.passengers,id(bus1.passengers))
# bus2 = HauntedBus()
# print(bus2.passengers,id(bus2.passengers))
# bus2.pick("yuan")
# bus2.passengers.append("san")
# print(bus2.passengers)
# print(bus1.passengers)

# import threading
# n = 0

# def add():
#     global n
#     for i in range(1000000):
#         n = n+1

# def sub():
#     global n 
#     for i in range(1000000):
#         n = n-1
# if __name__ == "__main__":
#     t1 = threading.Thread(target=add)
#     t2 = threading.Thread(target=sub)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("n的值:",n)

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




