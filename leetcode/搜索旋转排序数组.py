"""
1.hash 时间复杂度:O(n)
2.二分查找 O(logn)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # 1.相等
            if nums[mid] == target:
                return mid
            # 2.0-mid为递增区间
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 3.mid-n为递增区间
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
