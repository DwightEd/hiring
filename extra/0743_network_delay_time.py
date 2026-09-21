"""网络延迟时间
题意与思路：非负权有向图，从起点向所有点传播的最晚到达时间；Dijkstra 用最小堆。
复杂度：O((V+E) log(E+1)) 时间，O(V+E) 空间。
来源：https://leetcode.cn/problems/network-delay-time/
"""

from heapq import heappush,heappop

class Solution:
    def networkDelayTime(self,times,n,k):
        graph=[[] for _ in range(n+1)]
        for u,v,w in times: graph[u].append((v,w))
        distance=[float('inf')]*(n+1)
        distance[k]=0
        heap=[(0,k)]
        while heap:
            cost,node=heappop(heap)
            if cost!=distance[node]: continue
            for other,weight in graph[node]:
                if cost+weight<distance[other]:
                    distance[other]=cost+weight
                    heappush(heap,(distance[other],other))
        answer=max(distance[1:])
        return -1 if answer==float('inf') else answer
