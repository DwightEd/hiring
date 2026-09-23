"""拼多多截图题：边界、穷举/随机对照与四个 ACM 入口测试。"""
import itertools
from pathlib import Path
import random
import re
import shutil
import tempfile
import subprocess
import sys
import unittest

from companies.pinduoduo.shelf_moves import minimum_moves
from companies.pinduoduo.duoduo_string import longest_duoduo
from companies.pinduoduo.orchard_square import RangeAddMax, minimum_side
from companies.pinduoduo.bracket_queries import BracketTree

ROOT = Path(__file__).resolve().parents[1]


def brute_moves(values):
    dp = [0] + [len(values) + 1] * len(values)
    for end in range(1, len(values) + 1):
        for start in range(end):
            if len(set(values[start:end])) == 1:
                dp[end] = min(dp[end], dp[start] + 1)
    return dp[-1]


def brute_duoduo(s):
    best = 0
    for mask in range(1 << len(s)):
        kept = ''.join(ch for i, ch in enumerate(s) if mask >> i & 1)
        if re.fullmatch('a*b*a*', kept):
            best = max(best, len(kept))
    return best


def brute_square(points, required):
    best = 10**10
    for group in itertools.combinations(points, required):
        xs, ys = zip(*group)
        best = min(best, max(max(xs) - min(xs), max(ys) - min(ys)) + 1)
    return best


def brute_valid(text):
    balance = 0
    for ch in text:
        balance += 1 if ch == '(' else -1
        if balance < 0:
            return False
    return balance == 0


class TestShelfMoves(unittest.TestCase):
    def test_screenshot_input(self):
        self.assertEqual(minimum_moves([2, 2, 3, 3, 3, 1, 1, 2]), 4)

    def test_boundaries(self):
        self.assertEqual(minimum_moves([9]), 1)
        self.assertEqual(minimum_moves([2] * 100000), 1)
        self.assertEqual(minimum_moves([1, 2] * 50000), 100000)
        self.assertEqual(minimum_moves([2, 3, 2]), 3)

    def test_exhaustive_partitions(self):
        for n in range(1, 7):
            for values in itertools.product((1, 2, 3), repeat=n):
                self.assertEqual(minimum_moves(values), brute_moves(values))


class TestDuoduo(unittest.TestCase):
    def test_examples(self):
        for s, expected in [('abba', 4), ('babab', 3), ('aaaa', 4), ('bbbb', 4), ('a', 1), ('b', 1)]:
            self.assertEqual(longest_duoduo(s), expected)

    def test_exhaustive_subsequences(self):
        for n in range(1, 8):
            for chars in itertools.product('ab', repeat=n):
                s = ''.join(chars)
                self.assertEqual(longest_duoduo(s), brute_duoduo(s), s)

    def test_constraint_size(self):
        self.assertEqual(longest_duoduo('a' * 5000), 5000)
        self.assertEqual(longest_duoduo('b' * 5000), 5000)


class TestOrchard(unittest.TestCase):
    def test_grid_off_by_one(self):
        self.assertEqual(minimum_side([(1, 1), (2, 1)], 2), 2)
        self.assertEqual(minimum_side([(1, 1), (5, 1)], 2), 5)

    def test_sparse_coordinates(self):
        points = [(1, 1), (10**9, 1), (1, 10**9)]
        self.assertEqual(minimum_side(points, 1), 1)
        self.assertEqual(minimum_side(points, 2), 10**9)
        self.assertEqual(minimum_side(points, 3), 10**9)

    def test_same_x_and_y(self):
        self.assertEqual(minimum_side([(2, y) for y in (1, 2, 3, 10)], 3), 3)
        self.assertEqual(minimum_side([(x, 2) for x in (1, 2, 3, 10)], 3), 3)

    def test_square_example(self):
        self.assertEqual(minimum_side([(1, 1), (2, 1), (1, 2), (10, 10)], 3), 2)

    def test_random_subsets(self):
        rng = random.Random(922)
        grid = list(itertools.product(range(1, 11), repeat=2))
        for _ in range(400):
            points = rng.sample(grid, rng.randint(1, 9))
            required = rng.randint(1, len(points))
            self.assertEqual(minimum_side(points, required), brute_square(points, required), (points, required))

    def test_range_add_max(self):
        rng = random.Random(33)
        for n in range(1, 25):
            tree, plain = RangeAddMax(n), [0] * n
            for _ in range(100):
                left = rng.randrange(n)
                right = rng.randrange(left + 1, n + 1)
                # Coverage counts are nonnegative in this algorithm.
                delta = 1 if min(plain[left:right]) == 0 else rng.choice((-1, 1))
                tree.add(left, right, delta)
                for i in range(left, right):
                    plain[i] += delta
                self.assertEqual(tree.maximum[1], max(plain))


class TestBrackets(unittest.TestCase):
    def test_prefix_not_only_total(self):
        self.assertTrue(BracketTree('()').is_valid(0, 2))
        self.assertFalse(BracketTree(')(').is_valid(0, 2))

    def test_double_flip(self):
        text = '(()())()'
        tree = BracketTree(text)
        tree.flip(1, 7)
        tree.flip(1, 7)
        for left in range(len(text)):
            for right in range(left + 1, len(text) + 1):
                self.assertEqual(tree.is_valid(left, right), brute_valid(text[left:right]))

    def test_full_and_nested_flip(self):
        chars = list('(())()(()())')
        tree = BracketTree(''.join(chars))
        for left, right in [(0, 12), (1, 11), (3, 8), (0, 1), (11, 12), (0, 12)]:
            tree.flip(left, right)
            for i in range(left, right):
                chars[i] = ')' if chars[i] == '(' else '('
            for l in range(len(chars)):
                for r in range(l + 1, len(chars) + 1):
                    self.assertEqual(tree.is_valid(l, r), brute_valid(chars[l:r]))

    def test_exhaustive_initial_queries(self):
        for n in range(1, 8):
            for chars in itertools.product('()', repeat=n):
                tree = BracketTree(''.join(chars))
                for left in range(n):
                    for right in range(left + 1, n + 1):
                        self.assertEqual(tree.is_valid(left, right), brute_valid(chars[left:right]))

    def test_random_operations(self):
        rng = random.Random(444)
        for _ in range(250):
            n = rng.randint(1, 70)
            chars = [rng.choice('()') for _ in range(n)]
            tree = BracketTree(''.join(chars))
            for _ in range(120):
                left = rng.randrange(n)
                right = rng.randrange(left + 1, n + 1)
                if rng.random() < 0.55:
                    tree.flip(left, right)
                    for i in range(left, right):
                        chars[i] = ')' if chars[i] == '(' else '('
                else:
                    self.assertEqual(tree.is_valid(left, right), brute_valid(chars[left:right]))


class TestCLI(unittest.TestCase):
    def run_cli(self, filename, data):
        process = subprocess.run([sys.executable, str(ROOT / 'companies/pinduoduo' / filename)], input=data, text=True, capture_output=True, check=True)
        return process.stdout

    def test_shelf(self):
        self.assertEqual(self.run_cli('shelf_moves.py', '2\n8\n2 2 3 3 3 1 1 2\n1\n7\n'), '4\n1\n')

    def test_duoduo(self):
        self.assertEqual(self.run_cli('duoduo_string.py', 'abba\n'), '4\n')

    def test_orchard(self):
        self.assertEqual(self.run_cli('orchard_square.py', '4 3\n1 1\n2 1\n1 2\n10 10\n'), '2\n')

    def test_brackets(self):
        data = '4 7\n(())\nQ 1 4\nF 2 3\nQ 1 4\nF 1 4\nQ 1 4\nQ 2 3\nQ 1 1\n'
        self.assertEqual(self.run_cli('bracket_queries.py', data), 'YES\nYES\nNO\nYES\nNO\n')

    def test_brackets_no_queries(self):
        self.assertEqual(self.run_cli('bracket_queries.py', '1 1\n(\nF 1 1\n'), '')


class TestCppBrackets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which('g++')
        if compiler is None:
            raise unittest.SkipTest('未安装 g++；仅跳过 C++ 对照，Python 测试正常运行')
        cls.temp = tempfile.TemporaryDirectory()
        cls.binary = str(Path(cls.temp.name) / 'brackets')
        subprocess.run([compiler, '-O2', '-std=c++17', str(ROOT / 'companies/pinduoduo/bracket_queries.cpp'), '-o', cls.binary], check=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_random_operations(self):
        rng = random.Random(417)
        chars = [rng.choice('()') for _ in range(67)]
        lines = ['67 2000', ''.join(chars)]
        expected = []
        for _ in range(2000):
            left = rng.randrange(len(chars))
            right = rng.randrange(left + 1, len(chars) + 1)
            if rng.random() < 0.5:
                lines.append(f'F {left + 1} {right}')
                for i in range(left, right):
                    chars[i] = ')' if chars[i] == '(' else '('
            else:
                lines.append(f'Q {left + 1} {right}')
                expected.append('YES' if brute_valid(chars[left:right]) else 'NO')
        process = subprocess.run([self.binary], input='\n'.join(lines) + '\n', text=True, capture_output=True, check=True)
        self.assertEqual(process.stdout.splitlines(), expected)

    def test_single_and_full_interval(self):
        data = '4 7\n(())\nQ 1 4\nF 2 3\nQ 1 4\nF 1 4\nQ 1 4\nQ 2 3\nQ 1 1\n'
        process = subprocess.run([self.binary], input=data, text=True, capture_output=True, check=True)
        self.assertEqual(process.stdout, 'YES\nYES\nNO\nYES\nNO\n')


if __name__ == '__main__':
    unittest.main()
