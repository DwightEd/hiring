"""优化冒泡排序：原地升序，返回同一个列表。

来源：cv_note 2021 视觉算法社招面经，作者未披露具体公司。
每轮最后一次交换之后的后缀已就位；若没有交换，立即结束。
最好 O(n)，最坏 O(n²)，空间 O(1)；稳定。用于考察排序原理，非通用最优排序。
"""


def bubble_sort(nums):
    end = len(nums) - 1
    while end > 0:
        last = 0
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                last = i
        end = last
    return nums
