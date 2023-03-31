"""
1.暴力法,两层循环,时间复杂度为:O(n平方)
2.一层循环,根据历史,时间复杂度为:O(1)

float("inf")表示极大值,可以与数字作比较
flaot("-inf")表示极小值,可以与数字作比较


1e3
# 1000.0
1e-3
#0.001
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = int(1e9)
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - minPrices)
            minPrices = min(minPrices, prices)
        return maxProfit

