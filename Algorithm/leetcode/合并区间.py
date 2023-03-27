"""
1.排序,比较是否有重叠区间
时间复杂度为排序的复杂度
nlogn

"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1.排序
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 2.merged为空或不重叠,直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 3.重叠,与上一区间合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
