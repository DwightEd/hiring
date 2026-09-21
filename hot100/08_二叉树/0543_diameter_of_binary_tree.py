"""543. 二叉树的直径
题意：求二叉树任意两节点间的最长边数。
思路：后序计算左右高度，用高度和更新直径；显式调用帧避免深递归。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/diameter-of-binary-tree/
"""

class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        stack, returned, best = [[root, 0, 0]], 0, 0
        while stack:
            frame = stack[-1]
            node, state, left_height = frame
            if state == 0:
                frame[1] = 1
                returned = 0
                if node.left:
                    stack.append([node.left, 0, 0])
            elif state == 1:
                frame[2], frame[1] = returned, 2
                returned = 0
                if node.right:
                    stack.append([node.right, 0, 0])
            else:
                best = max(best, left_height + returned)
                returned = 1 + max(left_height, returned)
                stack.pop()
        return best
