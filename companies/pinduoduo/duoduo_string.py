"""多多字符串：a*b*a* 最长子序列。完整题面见 02_duoduo_string.md。
保留全部 a 为基线，中间区间保留 b、删除 a；最大化 #b-#a。
时间 O(n)，辅助空间 O(1)。
"""
import sys


def longest_duoduo(s: str) -> int:
    gain = best_gain = 0
    for ch in s:
        value = 1 if ch == 'b' else -1
        gain = max(0, gain + value)
        best_gain = max(best_gain, gain)
    return s.count('a') + best_gain


def main() -> None:
    s = sys.stdin.buffer.readline().strip().decode()
    print(longest_duoduo(s))


if __name__ == '__main__':
    main()
