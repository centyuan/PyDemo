"""
question:给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # 指向父节点


class Solution:
    nodes = []

    def GetNext(self, pNode):
        # 找出root节点
        root = pNode
        while root.next:
            root = root.next
        # 中序遍历
        self.inorder(root)
        #
        for i in range(len(self.nodes) - 1):
            if pNode == self.nodes[i]:
                return self.nodes[i + 1]

    def inorder(self, root):
        # 中序遍历
        if not root:
            return
        self.inorder(root.left)
        self.nodes.append(root)
        self.inorder(root.right)
