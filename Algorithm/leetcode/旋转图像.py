"""
1.遍历使用辅助数组 matrix[j][n-i-1] = matrix[i][j]
2.原地旋转
matrix[col][n-row-1] = matrix[row][col]
matrix[n-row-1][n-col-1] = matrix[col][n-row-1]
matrix[n-col-1][row] = matrix[n-row-1][n-col-1]
matrix[row][col] = matrix[n-col-1][row]
temp = matrix[n-col-1][row]
3.翻转,水平翻转+对角线翻转

"""
from typing import List


class Solution:
    # 1.使用辅助函数 O(n平方),O(n平方)
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        matrix[:] = matrix_new

    # 2.原地翻转 O(n平方),O(1)
    def rotate1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

    # 3.翻转代替旋转(水平翻转->对角线翻转)
    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 1.水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 2.对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
