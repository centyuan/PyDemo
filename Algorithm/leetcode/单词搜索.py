"""
回溯+递归
时间复杂度:MN+3的l次方
MN:为两层循环
3的l次方:为check(i,j,k),除第一次可以进入4个分支,其余时间最多进入三个分支,因为每个位置只能使用一次
空间复杂度:O(MN)
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 3.定义check
        def check(i: int, j: int, k: int) -> bool:
            # 不相等
            if board[i][j] != word[k]:
                return False
            # word单词遍历完
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < h and 0 <= newj < w and (newi, newj) not in visited:
                    if check(newi, newj, k + 1):
                        result = True
                        break
            visited.remove((i, j))
            return result

        # 1.初始化
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        h, w = len(board), len(board[0])
        # 2.遍历
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False
