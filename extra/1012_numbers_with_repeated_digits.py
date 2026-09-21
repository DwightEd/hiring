"""至少一位重复数字
题意与思路：数位 DP 统计 1..n 中所有数位互异的数，再用 n 减去；前导零不占数字位。
复杂度：O(log n·2^10·10) 时间，O(log n·2^10) 空间。
来源：https://leetcode.cn/problems/numbers-with-repeated-digits/
"""

from functools import lru_cache

class Solution:
    def numDupDigitsAtMostN(self,n):
        digits=list(map(int,str(n)))
        @lru_cache(None)
        def dfs(position,mask,tight,started):
            if position==len(digits): return int(started)
            limit=digits[position] if tight else 9
            answer=0
            for digit in range(limit+1):
                next_tight=tight and digit==limit
                if not started and digit==0:
                    answer+=dfs(position+1,mask,next_tight,False)
                elif not mask&(1<<digit):
                    answer+=dfs(position+1,mask|(1<<digit),next_tight,True)
            return answer
        return n-dfs(0,0,True,False)
