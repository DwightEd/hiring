"""79. 单词搜索
题意：判断能否通过四邻接且不重复使用格子拼出 word，恢复棋盘。
思路：DFS 临时标记已用格子，成功与失败返回前都还原。
时间：O(mn·3^L) 上界，L 为词长；空间：O(L)。
原题：https://leetcode.cn/problems/word-search/
"""

class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        def dfs(r, c, index):
            if board[r][c] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            saved, board[r][c] = board[r][c], None
            found = False
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] is not None:
                    if dfs(nr, nc, index + 1):
                        found = True
                        break
            board[r][c] = saved
            return found
        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
