"""
description:
有n阶楼梯,每次可以爬 1或2个台阶,有多少种方法可以爬到楼顶？
是一个斐波拉契数列
1.迭代+累加(动态转移即动态规划)
2.递归+hashmap(避免重复计算)
"""


class Solution:
    # 1. 迭代+累加
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        result, prePre, pre = 0, 1, 2
        for i in range(3, n):
            result = prePre + pre
            prePre = pre
            pre = result
        return result

    # 2.递归+hashmap
    hashmap = {}

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.hashmap.get(n):
            return self.hashmap.get(n)
        else:
            result = self.climbStairs2(n - 1) + self.climbStairs2(n - 2)
            self.hashmap[n] = result
            return result
