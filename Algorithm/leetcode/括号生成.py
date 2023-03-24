"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            # left:左括号还可以使用的数,right右括号还可以使用的数
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)
        dfs(cur_str,n,n)
        return res
