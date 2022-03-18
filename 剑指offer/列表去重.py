# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 16:43

#1.保留原来顺序
old_list = [1,2,3,2,3,4,5]
new_list = []
for i in old_list:
    if i not in new_list:
        new_list.append(i)
#2.字典去重
new_list = list(dict.fromkeys(old_list)) #fromkeys(必须参数，可选参数(默认为None))

