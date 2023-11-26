"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度，找出最多的数组中大小连续的数字

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

# 枚举数组中每个X,不断尝试匹配x+1,x+2...x+y, 不断枚举更新答案,利用hash去掉重复的x+x
# 跳过:枚举的数 xxx 一定是在数组中不存在前驱数x−1 的


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            # 不在才进去，在的话说明前面已经到过这个地方，在从这开始也不会比前面的那个大
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
