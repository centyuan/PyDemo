import bisect
from typing import List


class Solution:
    # 1.直接查找 O(nm)
    def findNumberIn2DArray(self, matrix: List[int], target: int) -> bool:
        x, y = 0, len(matrix[0]) - 1
        while x <= len(matrix) - 1 and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

    # 2.二分查找:对每一行使用二分查找 O(nlogm)
    def findNumberIn2DArray_2(self, matrix: List[int], target: int) -> bool:
        for row in matrix:
            id_x = bisect.bisect_left(row, target)  # 没找到返r回插入的位置
            if id_x < len(row) and row[id_x] == target:
                return True
        return False
