"""手写三路快速排序
题意与思路：随机枢轴三路分区，先处理小区间、大区间压栈，控制栈高度。
复杂度：O(n log n) 期望、O(n²) 最坏时间，O(log n) 栈空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

from random import Random

def quicksort(nums,seed=0):
    rng,stack=Random(seed),[(0,len(nums)-1)]
    while stack:
        left,right=stack.pop()
        while left<right:
            pivot=nums[rng.randrange(left,right+1)]
            low,index,high=left,left,right
            while index<=high:
                if nums[index]<pivot:
                    nums[low],nums[index]=nums[index],nums[low];low+=1;index+=1
                elif nums[index]>pivot:
                    nums[index],nums[high]=nums[high],nums[index];high-=1
                else: index+=1
            if low-left<right-high:
                stack.append((high+1,right));right=low-1
            else:
                stack.append((left,low-1));left=high+1
    return nums
