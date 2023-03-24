"""
0.暴力 O(n三次方)
1.动态规划 O(n),空间复杂度为O(n)
2.栈
"""


class Solution:
    # 1.栈
    def longestValidParentheses(self, s: str) -> int:
        maxLegth = 0  # 1.长度
        stack = [-1]  # 2.定义栈
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)  # 3.入栈
            else:
                stack.pop()  # 4.出栈
                # 5.栈是否为空
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxLegth = max(maxLegth, i - stack[-1])
        return maxLegth
