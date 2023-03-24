class Solution:
    # 1.直接查找 O(nm)
    def find(self, target, array):
        x, y = 0, len(array[0]) - 1
        while x <= len(array) - 1 and y >= 0:
            if array[x][y] == target:
                return True
            elif array[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
    # 2.二分查找:对每一行使用二分查找
