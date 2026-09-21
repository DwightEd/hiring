"""华为 2026-09-18 AI 方向：全局位与窗口注意力（用户截图 P5467）。
Q/K/V 都是 L×D 整数矩阵。全局位置读取全序列，其他位置读取全局集合与半径 W 窗口的并集。
只取点积严格为正的前 T 项；同分优先小下标。输出 sum(score*V)，不做 softmax 或 sqrt(D) 缩放。
核心 API 的题意已由截图核实。截图仅显示输入首行 L D G W T，后续字段顺序未展示；
本仓库练习 CLI 约定：首行之后为 G 个全局下标，再依次为 Q、K、V 各 L×D 个整数。
若原平台的后续顺序不同，只需调整 solve 中读取顺序。
时间 O(sum_i(|C_i|*D + |C_i|*log(T+1) + min(T,|C_i|)*D))；额外 O(G+T+D)，不计输入输出。
"""
from heapq import heappush, heapreplace
import sys


def global_window_attention(q, k, v, global_positions, window, top_t):
    length, dimension = len(q), len(q[0])
    global_set = set(global_positions)
    answer = []
    for i, query in enumerate(q):
        left, right = max(0, i-window), min(length, i+window+1)
        if i in global_set:
            candidates = range(length)
        else:
            # 全局与窗口重叠的下标仅出现一次；不生成 L×L 分数矩阵。
            candidates = (j for group in (global_set, range(left, right)) for j in group
                          if group is global_set or j not in global_set)
        heap = []
        for j in candidates:
            score = sum(a*b for a, b in zip(query, k[j]))
            if score <= 0 or top_t == 0:
                continue
            item = (score, -j)  # 堆顶是最差项：低分，或同分但下标大。
            if len(heap) < top_t:
                heappush(heap, item)
            elif item > heap[0]:
                heapreplace(heap, item)
        row = [0] * dimension
        for score, negative_index in heap:
            for x, value in enumerate(v[-negative_index]):
                row[x] += score * value
        answer.append(row)
    return answer


def solve():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    length, dimension, g, window, top_t = (next(values) for _ in range(5))
    positions = [next(values) for _ in range(g)]
    def matrix():
        return [[next(values) for _ in range(dimension)] for _ in range(length)]
    q, k, v = matrix(), matrix(), matrix()
    result = global_window_attention(q, k, v, positions, window, top_t)
    sys.stdout.write('\n'.join(' '.join(map(str, row)) for row in result) + '\n')


if __name__ == '__main__':
    solve()
