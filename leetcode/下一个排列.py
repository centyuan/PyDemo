"""
一.两遍扫描
时间复杂度:O(n)
空间复杂度:O(1)
步骤:
1.找较小值i,num[i]>=num[i+1]
2.找较大值j,num[i]>=num[j]
3.交换i,j
4.i+1,n反转
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


