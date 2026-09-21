"""循环数组下一个更大元素
题意与思路：扫描两遍下标，单调栈只在第一遍入栈，第二遍负责补齐跨边界答案。
复杂度：O(n) 时间和空间。
来源：https://leetcode.cn/problems/next-greater-element-ii/
"""

class Solution:
    def nextGreaterElements(self,nums):
        n=len(nums)
        result,stack=[-1]*n,[]
        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]: result[stack.pop()]=nums[i%n]
            if i<n: stack.append(i)
        return result
