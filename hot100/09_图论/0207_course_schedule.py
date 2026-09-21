"""207. 课程表
题意：判断有先修约束的全部课程能否完成。
思路：Kahn 拓扑排序反复去掉入度零节点；有剩余就存在有向环。
时间：O(V+E)；空间：O(V+E)。
原题：https://leetcode.cn/problems/course-schedule/
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph, degree = [[] for _ in range(numCourses)], [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degree[course] += 1
        queue = deque(i for i, d in enumerate(degree) if d == 0)
        finished = 0
        while queue:
            node = queue.popleft()
            finished += 1
            for other in graph[node]:
                degree[other] -= 1
                if degree[other] == 0:
                    queue.append(other)
        return finished == numCourses
