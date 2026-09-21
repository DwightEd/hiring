"""238. 除了自身以外数组的乘积
题意：不用除法，求每项以外所有数的乘积。
思路：输出数组先存左侧乘积，再用一个变量累计右侧乘积。
时间：O(n)；空间：O(1)，不计输出。
原题：https://leetcode.cn/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums):
        answer, prefix = [1] * len(nums), 1
        for i, value in enumerate(nums):
            answer[i] = prefix
            prefix *= value
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
