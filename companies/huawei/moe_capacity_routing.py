"""华为 AI 2026-07-24：MoE Top-K 路由与容量限制。
来源（公开回忆，非公司官方试卷）：https://www.nowcoder.com/discuss/914337978896384000
输入 N E K C，接着 N 行 E 个分数。每行选分数最高 K 个专家，同分先小下标。
按 token 顺序处理，每个专家最多接受 C 次；满容量丢弃，不补选其他专家。
输出负载平方和，再输出各专家负载。
时间 O(NE log(K+1))，按行处理时额外 O(E+K)。
"""
from heapq import nlargest
import sys


def route(score_rows, experts, top_k, capacity):
    load = [0] * experts
    for row in score_rows:
        selected = nlargest(top_k, range(experts), key=lambda j: (row[j], -j))
        for expert in selected:
            if load[expert] < capacity:
                load[expert] += 1
    return sum(value*value for value in load), load


def solve():
    n, e, k, capacity = map(int, sys.stdin.buffer.readline().split())
    rows = (list(map(int, sys.stdin.buffer.readline().split())) for _ in range(n))
    penalty, load = route(rows, e, k, capacity)
    print(penalty)
    print(*load)


if __name__ == '__main__':
    solve()
