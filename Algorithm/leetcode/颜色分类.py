"""
1.单指针+遍历,时间复杂度:O(n)两次遍历,空间复杂度O(1)
2.双指针+遍历,时间复杂度:O(n)一次遍历,空间复杂度O(1)

"""
from typing import List


class Solution:
    # 1.单指针
    def sortColors(self, nums: List[int]) -> None:
        n, ptr = len(nums), 0
        for i in range(n):
            # 交换0
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

        for i in range(ptr, n):
            # 交换1
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]

    # 2.双指针
    def sortColors(self, nums: List[int]) -> None:
        p0, p2, n = 0, len(nums), len(nums)
        i = 0
        while i <= p2:
            # 交换 2
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            # 交换 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
