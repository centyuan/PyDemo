# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 23:39

def compact(lst):
    return list(filter(bool,lst))

compact([0,1,False,2,'',3,'a','s',34])
#[1,2,3,'a','s',34]
