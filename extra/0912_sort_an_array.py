"""手写堆排序
题意与思路：原地建立最大堆，再将堆顶逐次换到末尾并缩小堆。
复杂度：最坏 O(n log n) 时间，O(1) 辅助空间。
来源：https://leetcode.cn/problems/sort-an-array/
"""

class Solution:
    def sortArray(self,nums):
        def down(root,end):
            while 2*root+1<end:
                child=2*root+1
                if child+1<end and nums[child+1]>nums[child]: child+=1
                if nums[root]>=nums[child]: return
                nums[root],nums[child]=nums[child],nums[root]
                root=child
        for root in range(len(nums)//2-1,-1,-1): down(root,len(nums))
        for end in range(len(nums)-1,0,-1):
            nums[0],nums[end]=nums[end],nums[0]
            down(0,end)
        return nums
