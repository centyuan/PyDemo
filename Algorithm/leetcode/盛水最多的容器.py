"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
"""
# 1.暴力解法

# 2.双指针
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1

        while l < r:
            ans = max(height[l], height[r]) * (r - l)
            area = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return area
