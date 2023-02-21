"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = SYMBOL_VALUES[ch]
            # 比后一个值小,减
            if i < n - 1 and value < SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans
