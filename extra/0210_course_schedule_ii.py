"""课程表顺序
题意与思路：Kahn 拓扑排序返回任意可行顺序，有环返回空列表。
复杂度：O(V+E) 时间和空间。
来源：https://leetcode.cn/problems/course-schedule-ii/
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        degree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            degree[a]+=1
        queue=deque(i for i in range(numCourses) if degree[i]==0)
        result=[]
        while queue:
            node=queue.popleft()
            result.append(node)
            for other in graph[node]:
                degree[other]-=1
                if degree[other]==0: queue.append(other)
        return result if len(result)==numCourses else []
