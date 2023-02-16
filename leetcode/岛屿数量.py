"""
岛屿数量:
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例:
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""
import collections
from typing import List


# 一:递归+dfs深度遍历
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1.判断是否为空
        if not grid:
            return 0
        result = 0
        row, col = len(grid), len(grid[0])
        # 2.循环找到1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    result += 1
                    # self.mark_dfs(grid, i, j)
                    self.mark_bfs(grid, i, j)
        return result

    # 深度搜索DFS+递归recursion
    def mark_dfs(self, grid, x, y):
        # 1.从(x,y)坐标开始标记周围1为0
        grid[x][y] = '0'
        # 左
        if x > 0 and grid[x - 1][y] == '1':
            self.mark_dfs(grid, x - 1, y)
        # 右
        if x < len(grid) - 1 and grid[x + 1][y] == '1':
            self.mark_dfs(grid, x + 1, y)
        # 上
        if y > 0 and grid[x][y - 1] == '1':
            self.mark_dfs(grid, x, y - 1)
        # 下
        if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
            self.mark_dfs(grid, x, y + 1)

    def mark_dfs1(self, grid, x, y):
        # 1.递归终止条件:超出边界可以或是'0'
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1 or grid[x][y] == '0':
            return
        # 2.标记为0
        grid[x][y] = '0'
        # 3.递归
        self.mark_dfs1(grid, x - 1, y)
        self.mark_dfs1(grid, x + 1, y)
        self.mark_dfs1(grid, x, y - 1)
        self.mark_dfs1(grid, x, y + 1)

    # 广度搜索BFS+queue
    def mark_bfs(self, grid, x, y):
        # 1.第一个点标记为0
        grid[x][y] = '0'
        # 2.第一个点坐标入队
        queue = collections.deque([(x, y)])
        while queue:
            # 3.左边弹出一个坐标
            current_x, current_y = queue.popleft()
            # 4.判断该坐标上下左右,为1:改为0并入队
            for i, j in [(current_x - 1, y), (current_x + 1, y), (current_x, current_y - 1),(current_x, current_y + 1)]:
                if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1 and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solu = Solution()
    print(solu.numIslands(grid))
