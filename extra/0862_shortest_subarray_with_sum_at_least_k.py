"""含负数的最短达标子数组
题意与思路：普通滑窗不适用；前缀和配单调队列，淘汰已结算的队首及被新前缀支配的队尾。
复杂度：O(n) 时间和空间。
来源：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
"""

from collections import deque

class Solution:
    def shortestSubarray(self,nums,k):
        queue=deque([(0,0)])
        prefix,best=0,len(nums)+1
        for i,value in enumerate(nums,1):
            prefix+=value
            while queue and prefix-queue[0][1]>=k:
                best=min(best,i-queue.popleft()[0])
            while queue and queue[-1][1]>=prefix: queue.pop()
            queue.append((i,prefix))
        return best if best<=len(nums) else -1
