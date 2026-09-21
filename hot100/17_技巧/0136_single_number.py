"""136. 只出现一次的数字
题意：每个整数出现两次，仅一个出现一次，找出它。
思路：异或满足交换律，x XOR x=0，全部异或后仅剩答案。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums):
        answer = 0
        for value in nums:
            answer ^= value
        return answer
