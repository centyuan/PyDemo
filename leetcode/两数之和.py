"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现
"""


class Solution:
    # 1.暴力法
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 2.hash表
    def twoSum1(self, nums, target):
        hash_table = dict((value, index) for index, value in enumerate(nums))
        print(hash_table)
        for value in hash_table.keys():
            print("value-target",value,target)
            if target - value in hash_table and target-value!=value:
                return hash_table[value], hash_table[target - value]
        return []


if __name__ == '__main__':
    solution = Solution()
    nums =[3,3]
    target = 6
    print(solution.twoSum1(nums, target))
