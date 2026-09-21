"""和为 k 的最长连续子数组（允许负数）。

来源：牛客华为大模型算法岗公开面经，2026-09-17。
https://www.nowcoder.com/discuss/931707110344130560
思路：prefix[j]-prefix[i]=k；同一前缀只记最早位置，使长度最大。
注意：这与 LC560 的“统计个数”不同，不能把最早下标改成频次。
时间 O(n) 期望；空间 O(n)。
"""


def max_length_sum_k(nums, k):
    first = {0: -1}
    total = answer = 0
    for i, value in enumerate(nums):
        total += value
        if total - k in first:
            answer = max(answer, i - first[total - k])
        first.setdefault(total, i)
    return answer
