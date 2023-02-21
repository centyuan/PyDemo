"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
三种方法:
1.排序,查找index不等于value的
2.hashmap:dict.get(index)
3.等差数列求和:Sn=n(a1+an)/2-sum()
"""

from typing import List


class Solution:
    # 1.排序
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    # 2.等差数列求和
    def missingNumber1(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums + 1))) // 2 - sum(nums)
