"""104. 二叉树的最大深度
题意：求二叉树最大深度，空树深度为零。
思路：显式 DFS 栈保存节点及其深度，避免退化树递归溢出。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/maximum-depth-of-binary-tree/
"""

class Solution:
    def maxDepth(self, root):
        stack = [(root, 1)] if root else []
        best = 0
        while stack:
            node, depth = stack.pop()
            best = max(best, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return best
