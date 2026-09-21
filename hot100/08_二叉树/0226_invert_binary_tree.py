"""226. 翻转二叉树
题意：原地翻转二叉树，交换每个节点的左右子树。
思路：每个节点恰好处理一次，用显式 DFS 栈。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/invert-binary-tree/
"""

class Solution:
    def invertTree(self, root):
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
