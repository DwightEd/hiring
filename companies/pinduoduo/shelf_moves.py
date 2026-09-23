"""货架最少搬运次数：统计连续等值段。完整题面见 01_shelf_moves.md。
时间 O(n)，算法辅助空间 O(1)；CLI 按测试组读取。
"""
import sys


def minimum_moves(values: list[int]) -> int:
    if not values:
        return 0
    moves = 1
    for i in range(1, len(values)):
        if values[i] != values[i - 1]:
            moves += 1
    return moves


def main() -> None:
    read = sys.stdin.buffer.readline
    test_cases = int(read())
    answers = []
    for _ in range(test_cases):
        n = int(read())
        values = []
        while len(values) < n:
            values.extend(map(int, read().split()))
        answers.append(str(minimum_moves(values)))
    sys.stdout.write('\n'.join(answers) + '\n')


if __name__ == '__main__':
    main()
