from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1.排序+双指针 时间复杂度:n平方
        if not nums or len(nums) < 3:
            return []
        n = len(nums)
        ans = []
        # 2.遍历第一个数
        for i in range(n):
            # 3.第一个数大于0
            if nums[i] > 0:
                return ans

            # 4.重复元素跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 5.双指针
            L = i + 1
            R = n - 1
            while L < R:
                # 6.三种情况
                if nums[i] + nums[L] + nums[R] == 0:
                    ans.append([nums[i], nums[L], nums[R]])
                    # 7.重复数字跳过
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    # 8.移动找下一个
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L = L + 1
                else:
                    R = R - 1
        return ans
