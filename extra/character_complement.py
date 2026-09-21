"""字符种类补集
题意与思路：返回 a 中出现而 b 中未出现的字符，按首次出现顺序去重；不是多重集合差。
复杂度：O(m+n) 期望时间，O(字符集大小) 空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

def character_complement(a,b):
    excluded,seen,result=set(b),set(),[]
    for ch in a:
        if ch not in excluded and ch not in seen:
            result.append(ch);seen.add(ch)
    return ''.join(result)
