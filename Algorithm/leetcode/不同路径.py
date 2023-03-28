"""
1.动态规划
动态转移方程f(i,j)代表从左上角走到(i,j)的路径总数量
f(i,j) = f(i-1,j)+f(i,j-1)
时间复杂度:O(nm)
空间复杂度:O(nm)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1.创建二维数组f
        """
        [1,1,1,1,1,1,1,1...n]
        [1,0.0,0,0,0,0,0...n]
        [1,0,0,0,0,0,0,0...n]
        ...
        [m,0,0,0,0,0,0,0...n]
        """
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # 2.从1开始循环
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
