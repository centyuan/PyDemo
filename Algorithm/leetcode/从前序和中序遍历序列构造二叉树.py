"""
1.递归
时间复杂度:O(n)
空间复杂度:O(n)
前序遍历:[根节点,[左子树前序遍历],[右子树前序遍历]]
中序遍历:[[左子树中序遍历],根节点,[右子树中序遍历]

"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1.非空判断
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        # 2.构建根节点,包括每个根子树节点
        root = TreeNode(preorder[0])
        # 3.找到中序遍历根节点, 左子树前序/中序遍历 迭代构建
        # 左子树前序遍历长度=左子树中序遍历长度
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                # 4.左子树前序遍历
                leftpre = preorder[1:i + 1]
                # 5.左子树中序遍历
                leftin = inorder[:i]
                # 6.构建左子树
                root.left = self.buildTree(leftpre, leftin)
                # 7.右子树
                rightpre = preorder[i + 1:]
                rightin = inorder[i + 1:]
                root.right = self.buildTree(rightpre, rightin)
                break
        return root
