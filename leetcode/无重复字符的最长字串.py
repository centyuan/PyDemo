"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


# 1.采用滑动窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        n = len(s)
        k, ans = -1, 0
        for i in range(n):
            if i != 0:
                lookup.remove(s[i - 1])
            while k + 1 < n and s[k + 1] not in lookup:
                # 不重复的,不断移动右指针
                lookup.add(s[k + 1])
                k += 1
            # 第i到k个字符是一个及长的无重复字符串
            ans = max(ans, k - i + 1)
        return ans
