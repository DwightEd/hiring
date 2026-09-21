"""单词接龙
题意与思路：每步换一个字母，中间词必须来自字典；双向 BFS 扩展较小边界。
复杂度：O(N·L²·26) 上界，计 Python 字符串构造；O(NL) 空间。
来源：https://leetcode.cn/problems/word-ladder/
"""

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words: return 0
        front, back, length = {beginWord}, {endWord}, 1
        words.discard(beginWord)
        words.discard(endWord)
        while front and back:
            if len(front)>len(back): front,back=back,front
            following=set()
            for word in front:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        candidate=word[:i]+ch+word[i+1:]
                        if candidate in back: return length+1
                        if candidate in words:
                            words.remove(candidate)
                            following.add(candidate)
            front=following
            length+=1
        return 0
