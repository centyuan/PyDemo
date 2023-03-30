"""
先前序遍历
在遍历修改
时间复杂度:O(n)
空间复杂度:O(n)

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]):
        preorderList = []

        def preorderTraversal(root):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        for i in range(1, len(preorderList)):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left, prev.right = None, curr
