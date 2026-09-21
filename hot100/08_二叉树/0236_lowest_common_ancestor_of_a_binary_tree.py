"""236. 二叉树的最近公共祖先
题意：求树中两个已存在节点 p、q 的最近公共祖先。
思路：显式后序帧模拟递归：两侧各找到一个则根为祖先，否则上传非空结果。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack, returned = [[root, 0, None]], None
        while stack:
            frame = stack[-1]
            node, state, left_result = frame
            if node is None or node is p or node is q:
                returned = node
                stack.pop()
            elif state == 0:
                frame[1] = 1
                stack.append([node.left, 0, None])
            elif state == 1:
                frame[2], frame[1] = returned, 2
                stack.append([node.right, 0, None])
            else:
                returned = node if left_result and returned else left_result or returned
                stack.pop()
        return returned
