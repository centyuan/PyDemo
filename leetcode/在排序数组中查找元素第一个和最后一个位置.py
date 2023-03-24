"""
1.暴力遍历 O(n)
2.二分  O(logn)

"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> int:
        # 1.返回第一个大于等于target位置
        # 2.放回第一个大于target的位置再-1
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 3.如果start存在,那么end
        end = self.lower_bound(nums, target)
        return [start,end]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1  # 左移
            else:
                left = mid + 1
        return left
