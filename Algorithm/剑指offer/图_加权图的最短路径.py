"""
狄克斯特拉算法(只适用于有向无环图):解决加权图中的最快路径
1.找出“最便宜”的节点,即可在最短时间内到达的节点
2.更新该节点的邻居的开销
3.重复这个过程
4.计算最终路径
如果图中包含负权边(使用贝尔曼-福德算法)
"""

graphs = {
    "乐谱": {"黑胶唱片": 5, "海报": 0},
    "黑胶唱片": {"低音吉他": 25, "架子鼓": 20},
    "海报": {"低音吉他": 30, "架子鼓": 35},
    "低音吉他": {"钢琴": 20},
    "架子鼓": {"钢琴": 10},
    "钢琴": {}
}
costs = {
    "黑胶唱片": 5,
    "海报": 0,
    "低音吉他": float("inf"),
    "架子鼓": float("inf"),
    "钢琴": float("inf"),
}
parents = {
    "黑胶唱片": "乐谱",
    "海报": "乐谱",
}
processed = []


def find_lowest_cost_node(costs):
    # float("inf")正无穷
    lowest_cost = float('inf')
    lowest_cost_node = None
    # 1.遍历所有节点
    for node in costs:
        cost = costs[node]
        # 2.如果当前节点开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find():
    # 1.未处理的节点找出开销最小的
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graphs[node]
        # 2.遍历当前节点所有邻居
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # 3.如果经当前节点前往邻居更近
            if costs.get(n) and costs.get(n) > new_cost:
                # 4.更新邻居的开销
                costs[n] = new_cost
                # 5.设置该邻居的父节点为当前节点
                parents[n] = node
        # 6.标记当前节点为已处理
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(costs)
    print(parents)


if __name__ == '__main__':
    find()
