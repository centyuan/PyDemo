"""
回溯算法+剪枝
"""
from typing import List


class Solution:
    # 1.
    def combinationSum(self, canditaes: List[int], target: int) -> List[List[int]]:
        def dfs(canditaes, begin, size, path, res, target):
            # begin 下一节点,去重
            if target < 0:
                return
            if target == 0:
                res.append(path)
            for index in range(begin, size):
                dfs(canditaes, index, size, path + [canditaes[index], res, target - canditaes[index]])

        size = len(canditaes)
        if not size:
            return []
        path, res = [], []
        dfs(canditaes, 0, size, path, res, target)
        return res

    # 2.排序剪枝
    def combinationSum2(self, canditaes: List[int], target: int) -> List[List[int]]:
        def dfs(canditaes, begin, size, path, res, target):
            if target == 0:
                res.append(path)
            for index in range(begin, size):
                new_target = target - canditaes[index]
                # 剪枝:减去一个数为负数,剪一个更大的数也为负数
                if new_target < 0:
                    break
                dfs(canditaes, index, size, path + [canditaes[index]], res, new_target)

        # 排序
        canditaes.sort()

        size = len(canditaes)
        if not size:
            return []
        path, res = [], []
        dfs()
        return res
