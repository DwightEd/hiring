"""200. 岛屿数量
题意：统计字符网格中四方向相连的陆地块数，修改输入网格。
思路：遇到尚未访问的陆地就计数，并用迭代洪泛抹去整个连通块。
时间：O(mn)；空间：O(mn) 最坏。
原题：https://leetcode.cn/problems/number-of-islands/
"""

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols, count = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != '1':
                    continue
                count += 1
                stack = [(i, j)]
                grid[i][j] = '0'
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            stack.append((nr, nc))
        return count
