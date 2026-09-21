"""94. 二叉树的中序遍历
题意：返回二叉树中序遍历序列。
思路：用显式栈模拟递归，先沿左链到底，再访问根和右子树。
时间：O(n)；空间：O(h)，h 为树高，不计输出。
原题：https://leetcode.cn/problems/binary-tree-inorder-traversal/
"""

class Solution:
    def inorderTraversal(self, root):
        stack, answer = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            answer.append(root.val)
            root = root.right
        return answer
