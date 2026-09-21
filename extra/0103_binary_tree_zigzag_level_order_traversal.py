"""二叉树锯齿层序遍历
题意与思路：BFS 按层收集，奇数层反转结果，节点处理顺序仍保持从左到右。
复杂度：O(n) 时间，O(w) 辅助空间。
来源：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
"""

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        queue = deque([root]) if root else deque()
        answer = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if len(answer)%2: level.reverse()
            answer.append(level)
        return answer
