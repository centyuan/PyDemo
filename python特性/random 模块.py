import random
import string
print(random.random()) #生成一个随机数 在[0,1)之间
print(random.randint(1, 10))  #1到10之间的随机整数
print(random.choice('tomorrow')) #从序列中随机取一个元素

print(random.randrange(0, 101, 2)) # 随机选取0到100间的偶数：
print(random.randrange(1,100,2) ) # 随机从1到100的间的奇数
# 多个字符中生成指定数量的随机字符：
print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
"""
string.ascii_letters    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits           0123456789
"""

# 多个字符中选取指定数量的字符组成新字符串：
print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.shuffle(items))