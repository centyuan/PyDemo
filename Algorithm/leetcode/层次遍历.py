"""
广度优先
时间复杂度:O(n)
空间复杂度:O(n)

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 层次遍历
        if not root:
            return []
        result, cur_nodes = [], [root]
        while cur_nodes:
            next_nodes = []
            res_level = []
            for node in cur_nodes:
                res_level.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            result.append(res_level)
            cur_nodes = next_nodes
        return result
