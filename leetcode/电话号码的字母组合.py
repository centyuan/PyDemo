"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
"""
# 1.递归+回溯
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1.为空
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = list()
        combination = list()

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combinations))
            else:
                digit =digits[index]
                for letter in phoneMap[digits]:
                    combination.append(letter)
                    backtrack(index+1)
                    combination.pop()
        backtrack(0)
        return combinations