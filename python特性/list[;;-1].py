# -*- coding:utf-8 -*-

# 倒序
var = 'abcde'
print('var[2]:',var[2])
print('var',var[:-1]) # abcd
print('var',var[-2:]) # de
print('var',var[::-1]) # edcba 倒序
print('var',var[1::-1]) # ba 第0,1的倒序
print('var',var[::-1][-2:]) # ba 先倒序，在去倒序两位
print('var',var[::-1][:-2]) # edc
print('var',var[0:2][::-1]) # 先取正两位，在倒序


tmp = [1, 2, 3, 4, 5, 6]
print(tmp[5::-2]) #[6,4,2]