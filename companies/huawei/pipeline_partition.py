"""华为 2026-09-18 AI 方向：流水线并行的最小峰值负载（用户截图 P5468）。
把 N 层正整数耗时，按原顺序切为恰好 K 个连续非空 stage，最小化最大段和。
约束 1<=K<=N<=500，1<=times[i]<=1000。输入 N K，接着 N 个耗时；输出最优最大负载。
二分答案+贪心：给定 limit，每段尽可能长，得到最少段数。
若最少段数<=K，因为全部耗时非负且 K<=N，继续拆分一定能得到恰好 K 段且不增大最大负载。
时间 O(N log(sum(times)-max(times)+1))，额外 O(1)。含负数时该贪心不成立。
"""
import sys


def minimum_peak(times, k):
    if not 1 <= k <= len(times) or any(x < 0 for x in times):
        raise ValueError('要求非负耗时且 1<=K<=N')
    left, right = max(times), sum(times)
    while left < right:
        limit = (left + right) // 2
        stages, load = 1, 0
        for value in times:
            if load + value > limit:
                stages += 1
                load = 0
            load += value
        if stages <= k:
            right = limit
        else:
            left = limit + 1
    return left


def split_exactly_k(times, k):
    """扩展：返回最优 limit 和恰好 K 个左闭右开区间，便于理解 <=K 的充分性。"""
    limit = minimum_peak(times, k)
    result, end, load = [], len(times), 0
    for i in range(len(times)-1, -1, -1):
        if load + times[i] > limit or i + 1 < k:
            result.append((i+1, end))
            end, load, k = i+1, 0, k-1
        load += times[i]
    result.append((0, end))
    return limit, result[::-1]


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    print(minimum_peak(data[2:2+n], k))


if __name__ == '__main__':
    solve()
