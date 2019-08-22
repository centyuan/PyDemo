#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-17 下午5:35
"""
例如要读取一份文件并返回每行的字符数,若采用列表推导来做,则需把文件每一行的长度都保存在内存中,
如果这个文件特别大,或通过无休止的network socket 来读取,或出现问题,占用大量内存
所以只适合处理少量的输入值
"""

value = [len(x) for x in open('../tempfile/my_file.txt')]
print(value)

#为了解决以上问题,python提供了生成器表达式,它是对列表推导和生成器的一种泛化,
#生成器表达式在运行时,并不会把整个输出序列都呈现出来,而是会估值为迭代器,(
#这个迭代器每次根据生成器表达式产生一项数据

#对生成器表达式求值时,它会立刻返回一个迭代器
it = (len(x) for x in open('../tempfile/my_file.txt'))
print(it)
for i in range(1,12):
    print(next(it))  #逐次调用内置的next函数

#生成器组合,生成器表达式返回的迭代器用作另一个生成器表达式的输入值
roots = ((x,x**2) for x in it)

#print(next(roots)) #外围的迭代器每次前进,都会推动内部那个迭代器
