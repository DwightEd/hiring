"""左侧全小右侧全大的元素
题意与思路：找所有严格大于全部左侧且小于全部右侧的元素下标；端点空侧条件视为成立。
复杂度：O(n) 时间和空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

def partition_pivots(nums):
    suffix=[float('inf')]*(len(nums)+1)
    for i in range(len(nums)-1,-1,-1): suffix[i]=min(nums[i],suffix[i+1])
    maximum,result=float('-inf'),[]
    for i,value in enumerate(nums):
        if maximum<value<suffix[i+1]: result.append(i)
        maximum=max(maximum,value)
    return result
