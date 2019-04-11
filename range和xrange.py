#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 上午11:03

"""
range 函数说明：range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。

"""
print(range(5))#[0,1,2,3,4]
#  xrange 函数说明：用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器。
#因为 python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可。
