"""199. 二叉树的右视图
题意：返回从右侧可见的各层最后一个节点值。
思路：右侧优先 DFS，每层第一次访问的节点就是右视图节点。
时间：O(n)；空间：O(h)，不计输出。
原题：https://leetcode.cn/problems/binary-tree-right-side-view/
"""

class Solution:
    def rightSideView(self, root):
        stack, answer = ([(root, 0)] if root else []), []
        while stack:
            node, depth = stack.pop()
            if depth == len(answer):
                answer.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return answer
