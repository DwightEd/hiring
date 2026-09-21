"""102. 二叉树的层序遍历
题意：返回按层分组的节点值。
思路：BFS 每轮固定当前队列长度，只处理这一层。
时间：O(n)；空间：O(w)，w 为最大层宽，不计输出。
原题：https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""

from collections import deque

class Solution:
    def levelOrder(self, root):
        queue = deque([root]) if root else deque()
        answer = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(level)
        return answer
