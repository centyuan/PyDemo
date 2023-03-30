"""
动态规划,时间复杂度 O(n平方) 空间复杂度O(n)
遍历1...n
1...i-1为左子树,i+1...n为右子树
i为根节点,则每个树不同
G(n)长度为n的不同二叉搜索树的个数
f(i,n) = G(i-1)*G(n-i)
G(n) = f(i,n)求和
"""


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[i - 1] * G[i - j]
        return G[n]
