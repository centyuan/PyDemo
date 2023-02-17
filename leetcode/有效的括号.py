"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if c == ")":
                        if temp !="(":
                            return False
                    if c == "}":
                        if temp !="{":
                            return False
                    if c == "]":
                        if temp !="]":
                            return False
        return True if len(stack)==0 else False