"""
Question
    你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
解决方案
    random 模块有大量的函数用来产生随机数和随机选择元素

"""
import random
values = [1,2,34,56,6,7]
# 随机抽取一个随机数
random.choice(values)
# 提取n个元素样本
random.sample(values,3)  # [1,34,6]
# 打乱顺序
random.shuffle(values)
# 生成(0-10)的随机整数
random.randint(0,10)
# 生成0-1内均匀分布的浮点数
random.random()
import string
print(string.ascii_lowercase)