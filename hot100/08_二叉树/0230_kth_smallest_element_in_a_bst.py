"""230. 二叉搜索树中第 K 小的元素
题意：求二叉搜索树中第 k 小的值，k 合法。
思路：中序遍历第 k 次弹出的节点就是答案，可以提前结束。
时间：O(h+k)；空间：O(h)。
原题：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
"""

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
