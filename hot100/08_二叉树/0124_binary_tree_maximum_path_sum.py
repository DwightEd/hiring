"""124. 二叉树中的最大路径和
题意：求非空二叉树中任意简单路径的最大节点和。
思路：向父节点只能上传单侧贡献，更新答案时可合并两侧；负贡献截为零。
时间：O(n)；空间：O(h)。
原题：https://leetcode.cn/problems/binary-tree-maximum-path-sum/
"""

class Solution:
    def maxPathSum(self, root):
        stack, returned, best = [[root, 0, 0]], 0, float('-inf')
        while stack:
            frame = stack[-1]
            node, state, left_gain = frame
            if state == 0:
                frame[1], returned = 1, 0
                if node.left:
                    stack.append([node.left, 0, 0])
            elif state == 1:
                frame[2], frame[1] = max(0, returned), 2
                returned = 0
                if node.right:
                    stack.append([node.right, 0, 0])
            else:
                right_gain = max(0, returned)
                best = max(best, node.val + left_gain + right_gain)
                returned = node.val + max(left_gain, right_gain)
                stack.pop()
        return best
