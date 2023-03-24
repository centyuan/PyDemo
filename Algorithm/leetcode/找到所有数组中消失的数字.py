"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，
并以数组的形式返回结果。
"""
# 利用数组本身下标为0-n
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n  # 已经增加过的,需要对n取模还原本来的值
            nums[x] += n  # 将出现的对于索引上的值+n
        ret = [i + 1 for i, v in enumerate(nums) if v <= n]
        return ret
