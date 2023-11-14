"""
schema:
一些操作处理小技巧
collections：高性能容量数据类型
"""

# 1.随机化列表 random.shuffle
from collections import Counter
from random import shuffle

x = ["Keep", "The", "Blue", "Flag"]
print(shuffle)

# 2.大写单词第一个字母
s = "programming is awesome"
print("第一个字母:", s.title())
print("全部大写", s.upper())

# 3.字符元素组成判定 collections.Counter,高性能个计数
if Counter("abcd3") == Counter("3acdb"):
    print("组成相同")

colors = ["red", "blue", "red", "green", "blue"]
print(Counter(colors))  # 对元素计数
# Counter({'red': 2, 'blue': 2, 'green': 1})\
# 出现次数最多的
print(Counter(colors).most_common()[0])
# 出现次数前三
print(Counter(colors).most_common(3))

# 4.字符串出现的次数
a = "python is a programming language. python is beautiful"
print(a.count("python"))

# 5.判断正整数
# ceil 返回上入整数:1.3返回2,int返回数字的下入整数:1.3返回1
value = 1.3
if type(value) == type(int(value)) and value > 0:
    print(True)

# 6.计算文件中大写字母的数量
with open("./Cap") as file:
    count = 0
    for i in file.read():  # 默认参数读取全部
        if i.isupper():
            count += 1
print(count)

# 7.列表的差,使用集合
c = ["a", "b", "C", "d"]
d = ["a", "b", "e", "f"]
print(set(c).difference(d))  # c中独有的
print(set(c) - set(d))  # c中独有的
print(set(d) - set(c))  # d中独有的

# 8.数组中最长的字符串
words = ["python", "java", "golang", "my_love###"]
print(max(words, key=len))

# 9.计算符
import operator
action = {
    "+":operator.add,
    "-":operator.sub,
    "/":operator.truediv,
    "*":operator.mul,
    "**":pow
}
