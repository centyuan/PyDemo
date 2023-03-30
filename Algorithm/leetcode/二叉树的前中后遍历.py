"""
广度遍历:层次遍历

深度遍历:
时间复杂度O(n),空间复杂度O(h),h为树的高度
1.前序遍历:根节点-左子树-右子树
2.中序遍历:左子树-根节点-右子树
3.后序遍历:左子树-右子树-根节点
"""

#  定义一个二叉树节点
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1.递归
    # 前序遍历__递归
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        left_data = self.preorderTraversal(root.left)
        right_data = self.preorderTraversal(root.right)
        return result + left_data + right_data

    # 中序遍历__递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        left_data = self.inorderTraversal(root.left)
        right_data = self.inorderTraversal(root.right)
        return left_data + result + right_data

    # 后序遍历__递归
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        left_data = self.postorderTraversal(root.left)
        right_data = self.postorderTraversal(root.right)
        return left_data + right_data + result

    # 2.迭代
    # 前序遍历__迭代
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 前序,right先入栈
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # 中序遍历__迭代
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    # 后序遍历__迭代,同前序遍历一样,结果反转
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
