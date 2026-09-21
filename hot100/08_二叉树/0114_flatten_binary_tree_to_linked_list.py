"""114. 二叉树展开为链表
题意：按前序顺序把树原地展开成只用 right 指针的链。
思路：将原右子树接到左子树最右节点，再把左子树整体移到右侧。
时间：O(n) 摊还；空间：O(1)。
原题：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
"""

class Solution:
    def flatten(self, root):
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = root.right
                root.right, root.left = root.left, None
            root = root.right
