"""98. 验证二叉搜索树
题意：验证整棵树是否是严格二叉搜索树。
思路：中序序列必须严格递增，重复值也不合法。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/validate-binary-search-tree/
"""

class Solution:
    def isValidBST(self, root):
        stack, previous = [], float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= previous:
                return False
            previous, root = root.val, root.right
        return True
