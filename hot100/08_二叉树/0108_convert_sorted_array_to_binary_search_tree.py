"""108. 将有序数组转换为二叉搜索树
题意：把升序数组转换为高度平衡的二叉搜索树。
思路：中点作根，索引区间递归处理两侧，不切片复制数组。
时间：O(n)；空间：O(log n)，不计输出。
原题：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            return TreeNode(nums[middle], build(left, middle - 1), build(middle + 1, right))
        return build(0, len(nums) - 1)
