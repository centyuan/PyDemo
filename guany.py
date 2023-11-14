# # # from collections import Counter
# #
# # w_d = Counter(st)
#
# st = "你好,我是coolfire"
#
#
# # class Solution:
# #     def tt(self, str_ex: str) -> None:
# #         hash_map = {}
# #         for item in str_ex:
# #             hash_map[item] += 1
# #         return hash_map
#
# # 2.num1 num2
# class Solution:
#     def sub(self, num1, num2) -> int:
#         new_num1 = list(num1).reverse()
#         new_num2 = list(num2).reverse()
#         result, add = [], 0
#         length = len(num1) if len(num1) < len(num2) else len(num2)
#         for index in range(length):
#             sum_d = int(new_num1[index]) + int(new_num2[index])
#             num = sum_d % 10  # 取模 返回除数的余数
#             result.append(num + add)
#             add = sum_d  10
#
#         add_ = new_num1 if len(new_num1) > len(new_num2) else new_num2
#         result.extend(add_[index:])
#         return result.reverse()


# 1、用lambda函数实现两个数相乘
import time

func = lambda a, b: a * b


# 2.利用while循环 完成1-100的整数数字相加和
def sum_100(number: int) -> int:
    sum = 0
    while number >= 1:
        sum += number
        number -= 1
    return sum


sum_100(100)


# 3. 请写一个函数，接受两个列表（list1，list2）作为参数，返回两个新的列表，
# 其中第一个列表包含list1和list2所有相同的元素，第二个列表包含list1和list2所有的不同元素。
def return_something(list1: list, list2: list) -> tuple:
    list1_, list2_ = set(list1), set(list2)
    common_ = list1_ & list2_
    different_ = list(list1_ - list2_) + list(list2_ - list1_)
    return common_, different_


# 4.输出结果
x = int(0.22)
x = 1


def foo():
    x = 2

    def innerfoo():
        x = 3
        print('local ', x)  # 3

    innerfoo()
    print('enclosing function locals ', x)  # 2


foo()
print('global ', x)  # 1


# 5.输出结果


class Ufo:
    def __init__(self):
        self.name = People

    def say(self):
        print("Ufo类", self.name)


class People:
    def __init__(self):
        self.name = People

    def say(self):
        print("People类", self.name)


class Animal:
    def __init__(self):
        self.name = Animal

    def say(self):
        print("Animal类", self.name)


class Person(Animal, People):
    pass


zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()


# 6.使用代码打印一下规律的数组
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]


# 规则:mark[i][j] = mark[i-1][j]+mark[i-1][j-1]
# 方法
def print_some():
    a = [[0] * i for i in range(1, 10)]
    for i in range(9):
        for j in range(i):
            if j == 0:
                a[i][j] = a[i - 1][j]
            if i == 0 or i == 1:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
            print(a[i][j])


print_some()


# 7.写一个函数，接受一个由int作为元素的list，找到最大值，禁止使用内置的或者list的max函数，
# 请手动实现max函数，分析复杂度，时间和空间效率越高越好(注意：尽量不要修改原始list)

def max_val(list1: list):
    # 1.一次循环,时间复杂度:O(n) 空间复杂度:O(1)常量空间
    result = 0
    for val in list1:
        if val > result:
            result = val
    return result


import copy

# def max_val2(list1: list):
#     # 2.排序,时间复杂度:为排序 O(log n)
#     new_list1 = copy.deepcopy(list1)
#     cur_val = 0
#     for val in new_list1:


# 8.写一个计时器函数来监控每个功能函数的运行时间
from functools import wraps


def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("消耗时间:", time.time() - start_time)
        return result

    return wrapper

















