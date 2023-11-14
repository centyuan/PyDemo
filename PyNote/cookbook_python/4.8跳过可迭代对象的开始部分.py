"""
读取一个文件，跳过文件开始部分的注释

"""
from itertools import dropwhile

with open('passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
# dropwhile 跳过# 注释部分
