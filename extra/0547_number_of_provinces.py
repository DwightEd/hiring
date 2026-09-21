"""省份数量
题意与思路：无向邻接矩阵的连通块数，并查集路径压缩与按大小合并。
复杂度：O(n² α(n)) 上界，O(n) 空间。
来源：https://leetcode.cn/problems/number-of-provinces/
"""

class Solution:
    def findCircleNum(self,isConnected):
        n=len(isConnected)
        parent,size=list(range(n)),[1]*n
        count=n
        def find(x):
            while x!=parent[x]: parent[x]=parent[parent[x]];x=parent[x]
            return x
        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    a,b=find(i),find(j)
                    if a!=b:
                        if size[a]<size[b]: a,b=b,a
                        parent[b]=a;size[a]+=size[b];count-=1
        return count
