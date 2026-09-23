"""括号串翻转与合法查询。完整题面及公式见 04_bracket_queries.md。
( 为 +1，) 为 -1。线段树保存总和、最小/最大前缀和（含空前缀）。
翻转是交换括号种类，不是反转字符顺序。
建树 O(n)，每次修改/查询 O(log n)，空间 O(n)。
"""
import sys


class BracketTree:
    def __init__(self, text: str):
        self.height = (len(text) - 1).bit_length()
        self.size = 1 << self.height
        self.total = [0] * (2 * self.size)
        self.low = [0] * (2 * self.size)
        self.high = [0] * (2 * self.size)
        self.lazy = bytearray(self.size)
        for i, ch in enumerate(text, self.size):
            value = 1 if ch == '(' else -1
            self.total[i] = value
            self.low[i] = min(0, value)
            self.high[i] = max(0, value)
        for node in range(self.size - 1, 0, -1):
            self._pull(node)

    def _pull(self, node: int) -> None:
        left, right = node * 2, node * 2 + 1
        total, low, high = self.total, self.low, self.high
        total[node] = total[left] + total[right]
        low[node] = min(low[left], total[left] + low[right])
        high[node] = max(high[left], total[left] + high[right])

    def _flip_node(self, node: int) -> None:
        self.total[node] = -self.total[node]
        self.low[node], self.high[node] = -self.high[node], -self.low[node]
        if node < self.size:
            self.lazy[node] ^= 1

    def _push(self, node: int) -> None:
        if self.lazy[node]:
            self._flip_node(node * 2)
            self._flip_node(node * 2 + 1)
            self.lazy[node] = 0

    def _push_boundaries(self, left: int, right: int) -> None:
        # 只下推被查询/修改边界穿过的祖先；整段使用的节点已经是最新汇总。
        for shift in range(self.height, 0, -1):
            if (left >> shift) << shift != left:
                self._push(left >> shift)
            if (right >> shift) << shift != right:
                self._push((right - 1) >> shift)

    def flip(self, left: int, right: int) -> None:
        """把 0-based 半开区间 [left, right) 内括号种类互换。"""
        left += self.size
        right += self.size
        self._push_boundaries(left, right)
        first, last = left, right
        while left < right:
            if left & 1:
                self._flip_node(left)
                left += 1
            if right & 1:
                right -= 1
                self._flip_node(right)
            left >>= 1
            right >>= 1
        # 只重算部分覆盖的祖先，不能覆盖刚刚整段翻转的节点。
        for shift in range(1, self.height + 1):
            if (first >> shift) << shift != first:
                self._pull(first >> shift)
            if (last >> shift) << shift != last:
                self._pull((last - 1) >> shift)

    def is_valid(self, left: int, right: int) -> bool:
        """判断 0-based 半开子串是否合法；奇数长度一定不合法。"""
        if (right - left) & 1:
            return False
        left += self.size
        right += self.size
        self._push_boundaries(left, right)
        total, low = self.total, self.low
        left_sum = left_low = right_sum = right_low = 0
        while left < right:
            if left & 1:
                left_low = min(left_low, left_sum + low[left])
                left_sum += total[left]
                left += 1
            if right & 1:
                right -= 1
                # 右侧找到的片段必须放到已有右侧结果的前面。
                right_low = min(low[right], total[right] + right_low)
                right_sum = total[right] + right_sum
            left >>= 1
            right >>= 1
        return left_sum + right_sum == 0 and min(left_low, left_sum + right_low) >= 0


def main() -> None:
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    tree = BracketTree(read().strip().decode())
    answers = []
    for _ in range(q):
        operation, left, right = read().split()
        # 题目的 1-based 闭区间 [l,r] -> 0-based 半开区间 [l-1,r)。
        left, right = int(left) - 1, int(right)
        if operation == b'F':
            tree.flip(left, right)
        else:
            answers.append('YES' if tree.is_valid(left, right) else 'NO')
    if answers:
        sys.stdout.write('\n'.join(answers) + '\n')


if __name__ == '__main__':
    main()
