"""最长重复子数组
题意与思路：沿两数组的每条对角线连续比较，断开便重置长度。
复杂度：O(mn) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/maximum-length-of-repeated-subarray/
"""

class Solution:
    def findLength(self,nums1,nums2):
        best=0
        for offset in range(-len(nums2)+1,len(nums1)):
            i,j=max(0,offset),max(0,-offset)
            current=0
            while i<len(nums1) and j<len(nums2):
                current=current+1 if nums1[i]==nums2[j] else 0
                best=max(best,current)
                i+=1;j+=1
        return best
