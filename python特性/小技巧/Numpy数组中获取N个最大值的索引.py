# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 23:03
import numpy as np

arr = np.array([1,2,2,4,5])
print(arr.argsort()[-3:][::-1])

# [4,3,1]
