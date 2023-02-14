from collections import defaultdict

# 1.
d = defaultdict(list)  # 里面是列表
d['key1'].append(1)
d['key2'].append(2)
d = defaultdict(set)  # 里面是集合
d['key3'].add(3)
d['key4'].add(4)

# 2.遇见以下情况可以使用上面的
d = {}
paires = {}
for key, value in paires:
    if key not in d:
        d[key] = []
    d[key].append(value)

# 3.OrderDict 控 制 一 个 字 典 中 元 素 的 顺 序
