"""78. 子集
题意：枚举互异整数数组的全部子集。
思路：处理每个数时，把已有每个子集增加一份包含该数的副本。
时间：O(n·2^n)，含输出；空间：O(n·2^n)，含输出。
原题：https://leetcode.cn/problems/subsets/
"""

class Solution:
    def subsets(self, nums):
        result = [[]]
        for value in nums:
            result += [part + [value] for part in result]
        return result
