"""416. 分割等和子集
题意：判断正整数数组能否分成和相等的两组。
思路：大整数位集的第 s 位表示能否达到和 s；每个数只用旧位集更新一次。
时间：O(n·S/w) 字运算量级，S 为目标和；空间：O(S/w) 机器字。
原题：https://leetcode.cn/problems/partition-equal-subset-sum/
"""

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable, mask = 1, (1 << (target + 1)) - 1
        for value in nums:
            if value <= target:
                reachable = (reachable | (reachable << value)) & mask
        return bool((reachable >> target) & 1)
