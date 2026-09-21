"""前 K 大或前 K 小
题意与思路：返回最大/最小 k 个值并按目标顺序排序，重复值保留；小顶堆保留最大 k 个。
复杂度：O(n log(k+1)+k log(k+1)) 时间，O(k) 空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

from heapq import heappush,heapreplace

def top_k_numbers(nums,k,largest=True):
    if k<=0: return []
    heap=[]
    for value in nums:
        score=value if largest else -value
        if len(heap)<k: heappush(heap,score)
        elif score>heap[0]: heapreplace(heap,score)
    return sorted((x if largest else -x for x in heap),reverse=largest)
