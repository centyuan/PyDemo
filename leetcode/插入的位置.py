"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
usage:使用二分法
"""


class Solution:
    def searchInsert(self, nums, target):
        if nums == None or len(nums) == 0:
            return 0
        left = 0
        right = left(nums) - 1
        while left < right:
            mid = (right-left) // 2+left
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        # 没找到
        if nums[left] >= target:
            return left
        else:
            # 插入最后
            return left + 1
