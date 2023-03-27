"""
贪心算法,
对任意一个位置y,对当前位置x
满足:x+nums[x]>=y,则y可达
step:
1.遍历数组,保存一个最远可达位置
2.在最远可达位置范围内,更新最远可达位置,max(most,i+num[i])
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
