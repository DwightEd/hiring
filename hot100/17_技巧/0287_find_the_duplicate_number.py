"""287. 寻找重复数
题意：n+1 个数均在 1..n，只有一个值重复，不能修改数组。
思路：把下标到 nums[index] 当作函数图，重复值就是从零出发的环入口。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        seeker = 0
        while seeker != slow:
            seeker, slow = nums[seeker], nums[slow]
        return seeker
