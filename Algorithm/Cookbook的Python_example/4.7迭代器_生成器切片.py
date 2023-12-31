import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# itertools.islice() 对其切片
for x in itertools.islice(c, 10, 20):
    print(x)

for y in itertools.islice(c, 10, None):
    # for y in itertools.islice(c,None,10):
    # None 表示从3-所有
    print(y)
"""
迭代器和生成器不能使用标准的切片操作，无索引
islice()通过遍历丢弃。
"""
