"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
"""
# 1.暴力解法

"""
2.双指针,最开始左右指针指向数组的左右两端
最开始:min(left,right)*(right-left)
第二步:移动较小的指针，如果相同，移动任意一个
第三步:直到两个指针重合
为什么
双指针代表的是 可以作为容器边界的所有位置的范围
时间复杂度：双指针最多遍历整个数组一次 O(n)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1

        while l < r:
            ans = min(height[l], height[r]) * (r - l)
            area = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return area
