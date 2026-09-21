"""295. 数据流的中位数
题意：支持动态加入整数和查询中位数。
思路：小顶堆存大半，负数小顶堆模拟大顶堆存小半，大小差不超过一。
时间：插入 O(log n)，查询 O(1)；空间：O(n)。
原题：https://leetcode.cn/problems/find-median-from-data-stream/
"""

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.low, self.high = [], []

    def addNum(self, num):
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))
        if len(self.high) > len(self.low):
            heappush(self.low, -heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
