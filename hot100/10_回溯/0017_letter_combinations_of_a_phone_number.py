"""17. 电话号码的字母组合
题意：枚举数字 2..9 对应的所有电话字母组合；空输入返回空列表。
思路：每轮给所有前缀追加当前数字的每种字母。
时间：O(n·4^n) 上界，含输出；空间：O(n·4^n)，含输出。
原题：https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = ['']
        for digit in digits:
            result = [prefix + ch for prefix in result for ch in mapping[digit]]
        return result
