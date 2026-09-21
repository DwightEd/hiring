"""有序列表公共元素
题意与思路：两个升序列表输出去重交集；各指针只前进。
复杂度：O(m+n) 时间，O(1) 辅助空间，不计输出。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

def sorted_intersection(a,b):
    i=j=0
    result=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]: i+=1
        elif a[i]>b[j]: j+=1
        else:
            if not result or result[-1]!=a[i]: result.append(a[i])
            i+=1;j+=1
    return result
