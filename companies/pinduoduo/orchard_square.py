"""果园最小收集边长。完整题面及证明见 03_orchard_square.md。
二分边长 + x 滑窗 + y 离散化 + 区间加/全局最大值线段树。
时间 O(n log n log U)，空间 O(n)，U 为覆盖全部苹果的边长。
坐标表示完整单元格：极差必须 < side，不能写成 <= side。
"""
import sys


class RangeAddMax:
    """只查询全局最大值；标记保留在父节点，不必下推。"""
    def __init__(self, n: int):
        self.size = 1 << (n - 1).bit_length()
        self.maximum = [0] * (2 * self.size)
        self.added = [0] * (2 * self.size)

    def add(self, left: int, right: int, delta: int) -> None:
        """给半开区间 [left, right) 加 delta。"""
        maximum, added = self.maximum, self.added
        left += self.size
        right += self.size
        first, last = left, right - 1
        while left < right:
            if left & 1:
                maximum[left] += delta
                added[left] += delta
                left += 1
            if right & 1:
                right -= 1
                maximum[right] += delta
                added[right] += delta
            left >>= 1
            right >>= 1
        # 每层先重算两个边界祖先，再向上；标记不会被覆盖。
        first >>= 1
        last >>= 1
        while first:
            child = first * 2
            maximum[first] = added[first] + max(maximum[child], maximum[child + 1])
            if last != first:
                child = last * 2
                maximum[last] = added[last] + max(maximum[child], maximum[child + 1])
            first >>= 1
            last >>= 1


def minimum_side(points: list[tuple[int, int]], required: int) -> int:
    if required == 1:
        return 1
    ordered = sorted(points)
    ys = sorted({y for _, y in ordered})
    rank = {y: i for i, y in enumerate(ys)}
    ranked = [(x, rank[y]) for x, y in ordered]
    upper = max(ordered[-1][0] - ordered[0][0], ys[-1] - ys[0]) + 1
    if required == len(points):
        return upper

    def feasible(side: int) -> bool:
        # 一颗位于 y 的苹果覆盖所有底边 b∈[y-side+1, y]。
        # 只枚举真实 y 坐标作为底边，预先算好每颗苹果的更新区间。
        starts = [0] * len(ys)
        first = 0
        for i, y in enumerate(ys):
            while y - ys[first] >= side:
                first += 1
            starts[i] = first
        tree = RangeAddMax(len(ys))
        left = 0
        for right, (x, yi) in enumerate(ranked):
            tree.add(starts[yi], yi + 1, 1)
            while x - ranked[left][0] >= side:
                old_yi = ranked[left][1]
                tree.add(starts[old_yi], old_yi + 1, -1)
                left += 1
            if right - left + 1 >= required and tree.maximum[1] >= required:
                return True
        return False

    lower = 1
    while lower < upper:
        middle = (lower + upper) // 2
        if feasible(middle):
            upper = middle
        else:
            lower = middle + 1
    return lower


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, required = data[:2]
    points = [(data[2 + 2*i], data[3 + 2*i]) for i in range(n)]
    print(minimum_side(points, required))


if __name__ == '__main__':
    main()
