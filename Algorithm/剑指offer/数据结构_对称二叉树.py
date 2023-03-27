# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-28 下午5:10
'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


# 二叉树镜像-->分别将交换结点的左子结点和右子结点交换，子结点还有子结点在交换(每一层)
class Sulotion:
    def isSymmetriacl(self, pRoot):
        if not pRoot:
            return True
        return self.checkTwoTree(pRoot.left, pRoot.right)
        pass

    def checkTwoTree(self, leftTree, rightTree):  # 递归
        if not leftTree and not rightTree:
            return True
        if not leftTree or not rightTree:
            return False
        if leftTree.val == rightTree.val:
            return self.checkTwoTree(leftTree.left, leftTree.right) and self.checkTwoTree(rightTree.left,
                                                                                          rightTree.right)
        return False

    def isSymmetriacl1(self, pRoot):  # 迭代

        """
        :type root: TreeNode
        :rtype: bool
        """
        if not pRoot:
            return True
        nodeList = [pRoot.left, pRoot.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True
