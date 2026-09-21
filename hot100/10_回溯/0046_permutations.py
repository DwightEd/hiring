"""46. 全排列
题意：枚举互异整数数组的全排列。
思路：原地交换确定每个位置，递归结束后交换还原。
时间：O(n·n!)，含输出；空间：O(n)，不计输出。
原题：https://leetcode.cn/problems/permutations/
"""

class Solution:
    def permute(self, nums):
        result = []
        def dfs(start):
            if start == len(nums):
                result.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)
        return result
