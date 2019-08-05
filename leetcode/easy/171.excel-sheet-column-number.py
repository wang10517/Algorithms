#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            curDigit = (ord(s[i]) - ord('A')) + 1
            result = result*(26)
            result += curDigit
        return result


print(Solution().titleToNumber('AAA'))
