"""283. 移动零
题意：原地将所有零移到末尾，保持非零元素相对顺序。
思路：写指针前方始终是处理过的非零前缀；最后补零。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/move-zeroes/
"""

class Solution:
    def moveZeroes(self, nums):
        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
