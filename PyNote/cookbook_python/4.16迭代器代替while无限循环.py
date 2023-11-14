import sys

f = open('passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

# iter()接受一个callable对象和一个结尾标记
# 知道返回值结尾标记值相等为止
"""
这种方式适用于从套字节和文件读取
"""