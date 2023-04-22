"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
1.动态规划:计算每一列的雨水相加,每一列取决于min(左右最高的)-自身高度
对数组height中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度
leftMax[0]=height[0]
rightMax[n-1]=height[n-1]
1<=i<=n-1,leftMax[i]=max(leftMax[i-1],height[i])
0<=i<=n-2,rightMax[i]=max(rightMax[i+1],height[i])
时间复杂度:O(n)
空间复杂度:O(n)要创建两个长度为n的数组leftMax/rightMax

2.遍历+双指针:优化了动态规划的空间复杂度
维护left/right两个指针,leftMax/rightMax两个变量
left向右移动,right向左移动,
时间复杂度:O(n)
空间复杂度:O(1)
有height[left]<height[right],必有leftMax<rightMax
有height[left]>=height[right],必有leftMax>=rightMax
"""
from typing import List


class Solution:
    # 1.动态规划:计算每一列的雨水相加
    def trap(self, height: List[int]) -> int:
        # 非空判断
        if not height:
            return 0
        n = len(height)
        # leftMax初始化及遍历查找
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        # rightmax初始化及其遍历查找
        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        # 求ans
        ans = sum([min(leftMax[i], rightMax[i]) - height[i] for i in range(n)])
        return ans

    # 2.遍历+双指针
    def trap1(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # 左边小,left移动
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans
