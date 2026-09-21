"""437. 路径总和 III
题意：统计从祖先向后代的连续路径和等于 targetSum 的路径数。
思路：当前根路径的前缀和计数；退出节点时撤销，避免跨兄弟子树串路径。
时间：O(n) 期望；空间：O(h)。
原题：https://leetcode.cn/problems/path-sum-iii/
"""

class Solution:
    def pathSum(self, root, targetSum):
        counts, answer = {0: 1}, 0
        stack = [(root, 0, False)] if root else []
        while stack:
            node, prefix, exiting = stack.pop()
            if exiting:
                counts[prefix] -= 1
                if counts[prefix] == 0:
                    del counts[prefix]
                continue
            prefix += node.val
            answer += counts.get(prefix - targetSum, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
            stack.append((node, prefix, True))
            if node.right:
                stack.append((node.right, prefix, False))
            if node.left:
                stack.append((node.left, prefix, False))
        return answer
