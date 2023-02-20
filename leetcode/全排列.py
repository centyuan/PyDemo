"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1.存放结果集
        result = []
        # 2.标记是否访问
        visited = dict.fromkeys(nums)
        # 3.递归放入result
        self.backTracking(nums, result, visited, [])
        # 4.返回result
        return result

    def backTracking(self, nums, result, visited, list_):
        # 1.长度相同,加入result,递归返回
        if len(nums) == len(list_):
            result.append(copy.deepcopy(list_))
            return
        for num in nums:
            # 2.访问不存在,加入list_`
            if not visited[num]:
                list_.append(num)
                visited[num] = True
                # 3.递归本身到下一层
                self.backTracking(nums, result, visited, list_)
                # 4.list_移除,visited置为False
                list_.pop(nums)
                visited[num] = False
