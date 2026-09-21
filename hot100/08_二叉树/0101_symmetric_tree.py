"""101. 对称二叉树
题意：判断二叉树左右是否镜像对称。
思路：成对比较外侧孩子和内侧孩子，结构为空的情况也要对应。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/symmetric-tree/
"""

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None or right is None:
                if left is not right:
                    return False
                continue
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
