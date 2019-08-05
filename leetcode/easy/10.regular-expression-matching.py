#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def processString(s):
        result = []
        for char in s:
            
    def isMatch(self, s: str, p: str) -> bool:
        ppt, spt = 0
        curS = p[spt]
        for ppt in range(len(p)):
            curP = p[ppt]
            if curS == curP:
                spt += 1
                curS = p[spt]
            else:
                if curP == ".":
                    ppt += 1
                    curP = p[ppt]
                elif curP == 
                    

                

