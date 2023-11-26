"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词：两个字符串包含的字母相同
示例1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# 1.排序法：互为字母异位词，对词排序后一定是相同的，将排序之后的字符串作为哈希表的键 时间复杂度: O(nklogk),n为字符串格个数,k为字符串最大长度
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            mp["".join((sorted(st)))].append(st)
        return list(mp.values())


# 2.计数:互为字母异位词，相同字母出现的次数一样
