# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
"""

题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
step 1：先根据前序遍历第一个点建立根节点。
step 2：然后遍历中序遍历找到根节点在数组中的位置。
step 3：再按照子树的节点数将两个遍历的序列分割成子数组，将子数组送入函数建立子树。
step 4：直到子树的 序列长度为0，结束递归。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):
        n = len(pre)
        m = len(vin)
        if n ==0 or m==0:
            return None
        # 构建根节点
        root = TreeNode(pre[0])
        for i in range(len(vin)):
            # 找到中序遍历中的前序第一个元素
            if pre[0] == vin[i]:
                # 1.左子树的前序遍历
                leftpre = pre[1:i+1]
                # 2.左子树的中序遍历
                leftvin = vin[:i]
                # 3.构建左子树
                root.left = self.reConstructBinaryTree(leftpre,leftvin)
                # 1.右子树的前序遍历
                rightpre = pre[i+1:]
                # 2.右子树的中序遍历
                rightvin = vin[i+1:]
                # 3.构建右子树
                root.right = self.reConstructBinaryTree(rightpre,rightvin)
                break
        return root
