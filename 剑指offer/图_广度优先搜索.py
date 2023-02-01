"""
a->b->e->g
a->c->d->e->g
a->c->f->e->g
广度优先查找最短路径
"""

from collections import deque

# 1.maps 记录各节点的子节点
maps = {
    'a': ['b', 'c'],
    'b': ['e'],
    'c': ['d', 'f'],
    'd': ['e'],
    'f': ['e'],
    'e': ['g'],
    'g': [],
}
# 2.起点终点
start = 'a'
end = 'g'
# 3.起始节点入队
my_deque = deque()
my_deque += maps[start]
# 4.定义已搜索,避免重复搜索
searched = []
# 5.维护所有搜索过的节点的父节点
parents = {
    'b': 'a',
    'c': 'a',
}
# 6.定义路径
path = [end]
# 7.搜索直到队列为空
while my_deque:
    location = my_deque.popleft()
    if location not in searched:
        if location == end:
            # 如果当前节点是终点，开始反推
            key = end
            while key !=start:
                farther = parents[key]
                path.append(farther)
                key = farther
            path.reverse()
        else:
            my_deque += maps[location]
            for v in maps[location]:
                # 只要当前点之前没有父亲，就把它写入parents表里，指定它的父亲。父亲唯一，不可变更(相当于短路径节点先进来,只记录短路径上的父节点)。
                if v not in parents:
                    parents[v] = location
            searched.append(location)
