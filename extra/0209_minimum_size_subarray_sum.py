"""长度最小的子数组
题意与思路：数组全为正，求和至少 target 的最短子数组；满足后尽量收缩窗口。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/minimum-size-subarray-sum/
"""

class Solution:
    def minSubArrayLen(self, target, nums):
        left=total=0
        best=len(nums)+1
        for right,value in enumerate(nums):
            total+=value
            while total>=target:
                best=min(best,right-left+1)
                total-=nums[left]
                left+=1
        return best if best<=len(nums) else 0
