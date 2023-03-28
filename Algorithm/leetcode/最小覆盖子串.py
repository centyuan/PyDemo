"""
1.滑动窗口
(1:i遍历,移动右指针,利用hash去包含所有t
(2:移动左指针去除多余的,记录最小值
(3:i+1,

"""
from collections import defaultdict


class Solution:
    def minWindwo(self, s: str, t: str):
        # 1.初始化,hash
        needCount, needs = len(t), defaultdict(int)
        for c in t:
            needs[c] += 1
        # 2.遍历
        l, res = 0, (0, 0)
        for r, v in enumerate(s):
            if needs[v] > 0:
                needCount -= 1  # 判断是否满足包含所有T元素
            needs[v] -= 1
            # 3.滑动窗口满足包含所有T元素
            if needCount == 0:
                # 4.增加l,移动左指针,收缩窗口
                while True:
                    # 5.判断是否可以收缩
                    if needs[s[l]] == 0:
                        break
                    needs[s[l]] += 1
                    l += 1
                # 6.记录最小值
                res = (l, r) if r - l < res[1] - res[0] else res
                # 7.移动左指针,寻找下一个
                needs[s[l]] += 1
                needCount += 1
                l += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]
