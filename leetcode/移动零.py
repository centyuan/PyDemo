"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
from typing import List


class Solution:
    # 1.采用快慢指针
    def moveZeros(self, nums: List[int]) -> None:
        slow, fast, n = 0, 0, len(nums)
        while fast < n:
            if nums[fast] != 0:
                # 交换两个值
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

