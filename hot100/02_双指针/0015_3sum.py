"""15. 三数之和
题意：返回所有和为零的不重复三元组。
思路：排序后固定一个数，双指针寻找另两个数；固定点和移动点分别去重。
时间：O(n²)；空间：O(n) Python 排序辅助空间，不计输出。
原题：https://leetcode.cn/problems/3sum/
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result
