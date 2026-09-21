"""4. 寻找两个正序数组的中位数
题意：求两个升序数组合并后的中位数，两数组不同时为空。
思路：在短数组上二分分割线，保证左半数量正确且左侧最大值不大于右侧最小值。
时间：O(log(min(m,n)+1))；空间：O(1)。
原题：https://leetcode.cn/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        left, right, half = 0, m, (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half - i
            al = a[i - 1] if i else float('-inf')
            ar = a[i] if i < m else float('inf')
            bl = b[j - 1] if j else float('-inf')
            br = b[j] if j < n else float('inf')
            if al > br:
                right = i - 1
            elif bl > ar:
                left = i + 1
            else:
                if (m + n) % 2:
                    return float(max(al, bl))
                return (max(al, bl) + min(ar, br)) / 2
