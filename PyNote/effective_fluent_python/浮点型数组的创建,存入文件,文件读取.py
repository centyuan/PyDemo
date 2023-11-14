from array import array
from random import random

"""需要一个只包含数字的列表，那么array.array 比list 更高效"""
# 创建 1000 万个随机浮点数
floats = array('d',(random() for i in range(10**7)))  # d：双精度浮点数
fp = open('floats.bin', 'wb') # wb 写 二进制
# 写入文件
floats.tofile(fp)
fp.close()
# 读取文件
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-2])
print(floats2==floats)

