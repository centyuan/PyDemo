"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
最大整数:float("inf")
最小整数:float("-inf")
"""
from typing import List


class Solution:
    # 1.暴力法
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        # 1.遍历
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                # 2.一个个累加
                sum = sum + nums[j]
                result = max(result, sum)
        return result

    # 3.动态规划
    def maxSubArray1(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            # 前面一个最大子序列和
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result
