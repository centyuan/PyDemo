"""
深度优先搜索+递归
左子树最大深度l,右子树最大深度r
=max(l,r)+1
时间复杂度:O(n)
空间复杂度:O(height) height为树的高度
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



