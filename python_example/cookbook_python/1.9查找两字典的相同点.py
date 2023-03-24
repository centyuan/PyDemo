"""
为了寻找两字典的相同点:
可以简单的两字典的keys()或items()执行集合操作
x & y 交集
x - y 查集        # 在x中不在y中
x | y 并集
x ^ y 对称查集    # 在x或y中，但不会同时出现在二者中
"""
a = {
    'x':1,
    'y':2,
    'z':3,
}
b = {
    'w':10,
    'x':11,
    'y':2,
}
# 一个字典就是一个key集合和一个value集合的映射关系
# keys返回一个展现键集合的键视图对象，支持集合操作
# items返回一个包含(key ,value)对的元素视图对象,支持集合操作
# values 不直接支持集合操作，需转换为set
a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()
# 过滤不想要的键
c = {key:a[key] for key in a.keys()-{'z','w'}}

