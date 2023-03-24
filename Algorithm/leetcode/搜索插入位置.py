"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 使用二分查找法
        if nums == None or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] >= target else left + 1
