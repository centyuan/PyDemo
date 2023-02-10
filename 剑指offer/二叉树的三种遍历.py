# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # 由于这里只是单纯的二叉树，而不是排序二叉树，所以不需要考虑数的大小关系等，
    # 也就是说可以按先后顺序插入顺序可以设计成root,root->left,root-rght这样，好处在于，
    # root插入后，root左右为空，这时插入root->left,然后再是root->right，
    # 这样能够确保root的2个子节点都有值，而不至于绕过root->rigth直接插入root->left->left
    # 这样的异常情况出现,具体实现我们使用list来模拟队列，root,root->left,root->right依次入队
    def add(self, data):  # add方法来把新的节点加进去
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            Treelist = [self.root]
            while True:
                point = Treelist.pop(0)  # 移除一个元素并返回
                if point.left == None:
                    point.left = node
                    return
                elif point.right is None:
                    point.right = node
                    return
                else:
                    Treelist.append(point.left)
                    Treelist.append(point.right)

    # 广度遍历->层次遍历

    def traverse1(self, root):  # 层次遍历
        if root is None:
            return None
        q = [root]
        res = [root.data]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.data)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.data)
        return res

    # 迭代
    def traverse2(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.data)
        return res

    # 深度遍历->
    # 前序遍历(根节点，左节点，右节点),
    # 中序遍历(左节点，根节点，右节点),
    # 后序遍历(左节点，右节点，根节点),

    # 递归
    def preorder1(self, root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.preorder1(root.left)
        right_data = self.preorder1(root.right)
        return result + left_data + right_data

    def preorder2(self, root, res=[]):
        if not root:  # 是否为空
            return
        res.append(root.data)
        self.preorder2(root.left, res)
        self.preorder2(root.right, res)
        return res

    # 迭代
    def preorder3(self, root):
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # 递归
    def inorder1(self, root):
        if not root:
            return []
        result = [root.data]
        left_data = self.inorder1(root.left)
        right_data = self.inorder1(root.right)
        return left_data + result + right_data

    def inorder2(self, root, res):
        if not root:
            return
        self.inorder2(root.left, res)
        res.append(root.data)
        self.inorder2(root.right, res)
        return res

    # 迭代
    def inorder3(self, root):
        stack = []
        node = root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.data)
            node = node.right

        return res

        pass

    # 递归
    def postorder1(self, root):
        if not root:
            return []
        result = [root.data]
        left_data = self.postorder1(root.left)
        right_data = self.postorder1(root.right)
        return left_data + right_data + result

    def postorder2(self, root, res):
        if not root:
            return
        self.postorder2(root.left, res)
        self.postorder2(root.right, res)
        res.append(root.data)
        return res

    def postorder3(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.data)
        return res[::-1]


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print(t.preorder1(t.root), end='')
    print(t.preorder3(t.root))

    print(t.inorder1(t.root), end='')
    print(t.inorder3(t.root))

    print(t.postorder1(t.root), end='')
    print(t.postorder3(t.root))

    print(t.traverse1(t.root), end='')
    print(t.traverse2(t.root))
