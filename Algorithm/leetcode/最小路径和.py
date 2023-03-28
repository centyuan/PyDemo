"""
1.动态规划
dp[i][j]表示从左上角到(i,j)位置的最小路径和,dp[0][0]=grid[0][0]
时间复杂度:O(nm)
空间复杂度:O(nm),可以优化到O(n),只存储上一行的值
i>0 and j=0:dp[i][0] =dp[i-1][0] + grid[i][0]
i=0 and j>0:dp[0][j] =dp[0][j-1] + grid[0][j]
i>0 and j>0:dp[i][j] =min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 1.非空判断
        if not grid or not grid[0]:
            return 0
        # 2.初始化
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, columns):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, columns):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # 3.遍历
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]
