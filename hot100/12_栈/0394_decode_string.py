"""394. 字符串解码
题意：解码合法的 k[内容] 嵌套重复表达式。
思路：先解析成语法树，再迭代展开，避免逐字符字符串拼接造成平方开销。
时间：O(n+M)，M 为解码长度；正重复数；空间：O(n+M)。
原题：https://leetcode.cn/problems/decode-string/
"""

class Solution:
    def decodeString(self, s):
        root, stack, number = [], [], 0
        current = root
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == '[':
                child = []
                current.append((number, child))
                stack.append(current)
                current, number = child, 0
            elif ch == ']':
                current = stack.pop()
            else:
                current.append(ch)
        pieces, frames = [], [(iter(root), root, 1)]
        while frames:
            iterator, sequence, remaining = frames[-1]
            item = next(iterator, None)
            if item is None:
                frames.pop()
                if remaining > 1:
                    frames.append((iter(sequence), sequence, remaining - 1))
            elif isinstance(item, str):
                pieces.append(item)
            else:
                count, child = item
                frames.append((iter(child), child, count))
        return ''.join(pieces)
