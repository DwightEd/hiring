"""平衡二叉树
题意与思路：后序计算高度，任一节点两侧高度差超过一即失败；用显式栈避免深递归。
复杂度：O(n) 时间，O(n) 空间。
来源：https://leetcode.cn/problems/balanced-binary-tree/
"""

class Solution:
    def isBalanced(self, root):
        stack, height = [(root, False)] if root else [], {None:0}
        while stack:
            node, visited = stack.pop()
            if visited:
                left, right = height[node.left], height[node.right]
                if abs(left-right)>1: return False
                height[node] = 1+max(left,right)
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
        return True
