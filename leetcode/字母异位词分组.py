"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
示例1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# 1.排序法
# 2.统计组成
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, sts: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in sts:
            mp["".join(sorted(st))].append(st)
        return list(mp.values())