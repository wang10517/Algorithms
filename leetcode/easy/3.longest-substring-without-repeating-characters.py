#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, start, last = 0, 0, 0
        hasDup = False
        ht = {}

        for end in s:
            if not end in ht:
                ht[end] = 1
                maxLen = max(maxLen, last - start + 1 )
            else:
                ht[end] += 1
                hasDup = True

            while hasDup:
                sChar = s[start]
                ht[sChar] -= 1
                if ht[sChar] == 0:
                    del ht[sChar]
                else:
                    hasDup = False
                start += 1
           
            last += 1
        return maxLen
