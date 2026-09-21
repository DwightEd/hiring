"""连接所有点的最小费用
题意与思路：完全图曼哈顿距离，朴素 Prim 不显式保存 n² 条边。
复杂度：O(n²) 时间，O(n) 空间；二维几何有更复杂的 O(n log n) 方法。
来源：https://leetcode.cn/problems/min-cost-to-connect-all-points/
"""

class Solution:
    def minCostConnectPoints(self,points):
        n=len(points)
        best,used=[float('inf')]*n,[False]*n
        best[0]=0
        total=0
        for _ in range(n):
            node=min((i for i in range(n) if not used[i]),key=lambda i:best[i])
            total+=best[node];used[node]=True
            x,y=points[node]
            for i,(a,b) in enumerate(points):
                if not used[i]: best[i]=min(best[i],abs(x-a)+abs(y-b))
        return total
