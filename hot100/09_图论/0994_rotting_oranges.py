"""994. 腐烂的橘子
题意：每分钟腐烂向四邻新鲜橘子传播，求全部腐烂时间。
思路：所有初始腐烂点一起入队做多源 BFS；剩余新鲜数判断不可达。
时间：O(mn)；空间：O(mn)。
原题：https://leetcode.cn/problems/rotting-oranges/
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols, fresh = len(grid), len(grid[0]), 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
