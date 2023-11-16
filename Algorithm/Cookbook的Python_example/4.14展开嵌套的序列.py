"""
展开嵌套的序列
"""
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        # isinstance(x,ignore_types)用來排除字符串和字节，防止将其展开成单个字符
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            # 或者
            # for i in flatten(x):
            #    yield i
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)
