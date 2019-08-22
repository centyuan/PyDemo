#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午6:22


#内置enumerate,可以把各种可迭代对象(迭代器)包装成生成器
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i,flavor in enumerate(flavor_list):
    print(('%d:%s' % (i,flavor)))

for i,flavor in enumerate(flavor_list,1): #指定开始计数的值,默认为0
    print('%d:%s' % (i,flavor))

"""
要点:
enumerate函数提供了一种精简的写法,可以在遍历迭代器时获知每个元素的索引
尽量用enumerate来改写那种将range与下标访问相结合的序列遍历代码
可以给enumerate提供第二个参数,以指定开始计数时所用的值(默认为0)

"""
