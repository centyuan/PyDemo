"""
时间复杂度:每个节点最多被访问一次O(n)
空间复杂度:为每一层递归函数分配栈空间,O(树的高度),最坏为O(n)
递归 lower,upper,
左子树不为空,则左子树所有节点值均小于它的根节点的值
右子树不为空,则右子树所有节点值均大于它的根节点的值
它的左右子树也为二叉搜索树

右子树:大于上上层,小于上层
左子树:小于上上层,大于上层
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")):
            # 递归终止条件
            # 1.都为空,返回True
            # 2.一个为空,返回False
            # 3.值不相等,返回False
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(root.left, lower, node.val):
                return False
            if not helper(root.right, node.val, upper):
                return False
            return True

        return helper(root)
