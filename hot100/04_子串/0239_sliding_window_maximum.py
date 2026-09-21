"""239. 滑动窗口最大值
题意：返回每个长度 k 的滑动窗口的最大值。
思路：单调队列存下标：淘汰过期下标和永远不可能胜出的较小值。
时间：O(n)，每个下标入出队各一次；空间：O(k)，不计输出。
原题：https://leetcode.cn/problems/sliding-window-maximum/
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        queue, result = deque(), []
        for i, value in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= value:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
